from pymongo import MongoClient
from bson.objectid import ObjectId
from linkedlist import LinkedList, Node # <-- Import LinkedList and Node classes
from queue_module import FlashcardQueue # <-- Import FlashcardQueue class
from datetime import datetime
from linkedlist import LinkedList, Node 
from queue_module import FlashcardQueue

class FlashcardDB:
    def __init__(self, connection_string, db_name="flashcard_app", collection_name="flashcards"):
        """Initializes the database connection."""
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.linked_list = LinkedList()
        self.queue = FlashcardQueue() 
        self.load_cards_into_linked_list()
        self.load_cards_into_queue()

    def load_cards_into_linked_list(self):
        """Loads all cards from MongoDB into the in-memory linked list."""
        all_cards = self.collection.find()
        for card_data in all_cards:
            new_node = self.linked_list.add_card(card_data['question'], card_data['answer'])
            new_node.card_id = card_data['_id']

    def load_cards_into_queue(self):
        """Loads all cards from MongoDB into the in-memory queue."""
        all_cards = self.collection.find()
        for card_data in all_cards:
            node = Node(card_data['_id'], card_data['question'], card_data['answer'])
            self.queue.enqueue_card(node)

    def add_card_to_db(self, question, answer):
        """Adds a card to both the DB and the linked list."""
        card_document = {"question": question, "answer": answer}
        result = self.collection.insert_one(card_document)
        new_node = self.linked_list.add_card(question, answer)
        new_node.card_id = result.inserted_id
        self.queue.enqueue_card(new_node)
        print(f"Card added with ID: {result.inserted_id}")
        return new_node

    def edit_card_in_db(self, card_id, new_question, new_answer):
        """Edits a card in the DB and the linked list."""
        if self.linked_list.edit_card(card_id, new_question, new_answer):
            self.collection.update_one(
                {"_id": card_id},
                {"$set": {"question": new_question, "answer": new_answer}}
            )
            print(f"Card {card_id} updated.")
            return True
        return False

    def delete_card_from_db(self, card_id):
        """Deletes a card from the DB and the linked list."""
        if self.linked_list.delete_card(card_id):
            self.collection.delete_one({"_id": card_id})
            print(f"Card {card_id} deleted.")
            return True
        return False

# Example Usage:
if __name__ == '__main__':
    # Replace with your actual connection string
    MONGO_URI = "mongodb+srv://mmuwale12:12345@flashcardappcluster.sqpcmki.mongodb.net/?retryWrites=true&w=majority&appName=FlashCardAppCluster"

    flashcard_manager = FlashcardDB(MONGO_URI)
    new_flashcard_node = flashcard_manager.add_card_to_db("What is Python?", "A high-level programming language.")

    flashcard_manager.queue.show_queue()

    print("\nDequeueing a card...")
    card = flashcard_manager.queue.dequeue_card()
    if card:
        print(f"Dequeued: {card.question} -> {card.answer}")
