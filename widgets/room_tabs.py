import customtkinter as ctk # type: ignore
from PIL import Image

def create_room_tabs(root):
    rooms = [
        {"name": "Living Room", "image": "living-room.jpg"},
        {"name": "Dining Room", "image": "dining-room.jpg"},
        {"name": "Bed Room 1", "image": "bed-room1.jpg"},
        {"name": "Bed Room 2", "image": "bed-room2.jpg"},
        {"name": "Garage", "image": "garage.jpg"}
    ]

    frame = ctk.CTkFrame(root, width=920, height=420)
    frame.place(x=20, y=360)

    ctk.CTkLabel(frame, text="My Rooms", font=("Arial", 26), text_color='#FDFEFE').place(x=20, y=10)
    tabview = ctk.CTkTabview(frame, width=880, height=365, fg_color='transparent')
    tabview.place(x=20, y=40)

    for room in rooms:
        tab = tabview.add(room["name"])
        room_img = ctk.CTkImage(light_image=Image.open(f"images/{room['image']}"), size=(440, 160))
        ctk.CTkLabel(tab, image=room_img, text="").place(x=10, y=0)

        devices = [
            {"name": "Lights", "image": "lights.png", "x": 470, "y": 0},
            {"name": "Speakers", "image": "speaker.png", "x": 670, "y": 0},
            {"name": "Curtains", "image": "curtains.png", "x": 470, "y": 155},
            {"name": "Humidifier", "image": "humidifier.png", "x": 670, "y": 155}
        ]

        for d in devices:
            f = ctk.CTkFrame(tab, width=190, height=145, fg_color="#333333")
            f.place(x=d["x"], y=d["y"])

            icon = ctk.CTkImage(light_image=Image.open(f"images/{d['image']}"), size=(80, 80))
            ctk.CTkLabel(f, image=icon, text="").place(x=10, y=10)

            default = "Open" if d["name"] == "Curtains" else "On"
            state_var = ctk.StringVar(value=default)
            switch = ctk.CTkSwitch(f, text="", variable=state_var,
                                   onvalue=default, offvalue="Closed" if default == "Open" else "Off",
                                   command=lambda r=room["name"], n=d["name"], v=state_var: print(f"{r} {n} toggled to {v.get()}"))
            switch.place(x=145, y=10)

            wifi_icon = ctk.CTkImage(light_image=Image.open("images/wifi.png"), size=(15, 15))
            plug_icon = ctk.CTkImage(light_image=Image.open("images/power-plug.png"), size=(15, 15))
            ctk.CTkLabel(f, image=wifi_icon, text="").place(x=160, y=40)
            ctk.CTkLabel(f, image=plug_icon, text="").place(x=160, y=60)

            ctk.CTkLabel(f, text=d["name"], font=("Arial", 18), text_color='#FDFEFE').place(x=15, y=98)
            ctk.CTkLabel(f, textvariable=state_var, font=("Arial", 12), text_color='#FDFEFE').place(x=15, y=120)

        # Music Player
        music_frame = ctk.CTkFrame(tab, width=440, height=140, fg_color="#333333")
        music_frame.place(x=10, y=170)

        album_icon = ctk.CTkImage(light_image=Image.open("images/music.png"), size=(110, 110))
        ctk.CTkLabel(music_frame, image=album_icon, text="").place(x=15, y=15)

        ctk.CTkLabel(music_frame, text="Music Title", font=("Arial", 20), text_color='#FDFEFE').place(x=140, y=10)
        ctk.CTkLabel(music_frame, text="Artist", font=("Arial", 16), text_color='#FDFEFE').place(x=140, y=35)

        progress = ctk.CTkProgressBar(music_frame, orientation='horizontal')
        progress.place(x=140, y=90)

        ctk.CTkLabel(music_frame, text="1:24", font=("Arial", 12), text_color='#FDFEFE').place(x=140, y=100)