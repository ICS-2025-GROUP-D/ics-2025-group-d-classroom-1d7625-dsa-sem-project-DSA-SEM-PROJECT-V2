# Flashcard Application - Maria and her Minions

| Name             | Admission Number |
|------------------|------------------|
| Maria Muwale     | 192414           |
| Nathan Achar     | 189206           |
| Githinji Mugambi | 189596           |
| Allan Waithaka   | 191604           |
| Faith Muthoni    | 178509           |

---

## What exactly does our project do?

Our project implements a flashcard study tool that mimics how learners use revision cards — flipping through them, going back, tagging useful ones, and dynamically updating the collection. We used four key data structures — **linked list**, **queue**, **stack**, and **hash map** — to model this behavior. MongoDB was used to store flashcards in the cloud.

---

## Which structures did we use and why?

| Data Structure | Usage                              | Why We Used It |
|----------------|-------------------------------------|----------------|
| **Linked List** | Flashcard storage in memory        | Dynamic and flexible add/edit/delete |
| **Queue**       | Review flow (FIFO order)           | Mimics normal flashcard flow |
| **Stack**       | Flip-back or "undo" feature        | Follows LIFO for card history |
| **Hash Map**    | Bookmarks & tag-based lookup       | Allows instant access to key cards |

---

## Which technologies were used to achieve our project?

- Python 3
- MongoDB Atlas (NoSQL cloud database)
- `pymongo` (MongoDB Python driver)
- Git & GitHub (collaboration & version control)
- Tkinter GUI

---

## Which group member handled which module?

### Maria Muwale – Queue (Review Flow)
- Created `FlashcardQueue` class using doubly-linked Nodes
- Implemented enqueue, dequeue, peek, and display methods

### Faith Muthoni – Stack (Flip History)
- Created `FlashcardStack` class with `push`, `pop`, and `peek`
- Integrated stack updates into the review loop for backtracking
- Tracked previously reviewed flashcards for LIFO-based undo

### Githinji Mugambi – Hash Map (Bookmarks)
- Designed dictionary-based tag/bookmark system for cards
- Linked cards to topics or "starred" labels
- Enabled instant retrieval of bookmarked cards
- Enabled the ability to review history

### Nathan Achar – Linked List (Card Storage) + MongoDB
- Built the `LinkedList` and `Node` classes for dynamic card management
- Enabled addition, editing, and deletion of flashcards
- Served as the backbone for queue and stack modules
- Set up MongoDB database for storage of data in a cloud platform

### Allan Waithaka – Interface + Integration
- Built the CLI menu to allow user interaction
- Integrated all modules: database, queue, stack, bookmarks
- Tested end-to-end functionality and handled edge cases

---

## Time and Space Complexity Summary

| Data Structure | Operation           | Time Complexity | Space Complexity | 
|----------------|---------------------|------------------|------------------|
| **Queue**      | Enqueue             | O(1)             | O(1)             |
|                | Dequeue             | O(1)             | O(1)             |
|                | Peek                | O(1)             | O(1)             |
|                | Show All            | O(n)             | O(1)             |
| **Stack**      | Push                | O(1)             | O(1)             |
|                | Pop                 | O(1)             | O(1)             |
|                | Peek                | O(1)             | O(1)             |
| **Linked List**| Add Card            | O(1)             | O(1)             |
|                | Edit/Delete/Search  | O(n)             | O(1)             |
|                | Display All         | O(n)             | O(1)             |
| **Hash Map**   | Add Bookmark        | O(1)             | O(1)             |
|                | Remove Bookmark     | O(1)             | O(1)             |
|                | Lookup Bookmark     | O(1)             | O(1)             |
|                | Get All Bookmarks   | O(k)             | O(k)             |


## A simple structure of how we handled our project

MongoDB Atlas
     ↓
Linked List (in-memory card storage)
     ↓
Queue (Review Order) <-> Stack (Undo History)
     ↓
Hash Map (Bookmarks/Tags)
     ↓
Interface (Tkinter)

## What challenges did we face and how did we solve them?
- Connecting to MongoDB brought issues with internet connection
- Understanding the Tkinter library was hard at first, but we managed to come up with a simple interface for our project
- Githinji couldn't work on his initial branch, and if it is deleted, his pull requests will be lost, therefore he resorted to having 2 branches

## References used
Python Tkinter - GeeksforGeeks https://share.google/auR7N0TiMX3kKpDKx
https://cloud.mongodb.com/v2/686543a330bb7741eb21af3c#/explorer/686622ee77ada12f30b63504/flashcard_app/flashcards/find

## How our interface looks
![Adding a flashcard]()
![Viewing the flashcard]()
![Viewing the categories/bookmarks]()
![Review history]()

## Steps for running our project
1. Ensure you have python 3 installed, a stable internet connection and MongoDB in the main file. If you don't have MongoDB, run `pip install pymongo`.
2. Run the app using `python main.py`