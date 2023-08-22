from telegram import (
    user,
    chat,
    photo_size,
    audio,
    document,
    video,
    voice,
    contact,
    dice,
    location,
    message,
)


user = user.User(123456789, False, "John", "Doe", "johndoe")
# print(user)

chat = chat.Chat(123456789, "private", "John", "Doe", "johndoe")
# print(chat)

photo_size = photo_size.PhotoSize("123456789", "123456789", 100, 100, 100)
# print(photo_size)

audio = audio.Audio("123456789", "123456789", 100)
# print(audio)

document = document.Document("123456789", "123456789", "Hello, World!")
# print(document)

video = video.Video("123456789", "123456789", 100, 100, 100)
# print(video)

voice = voice.Voice("123456789", "123456789", 100)
# print(voice)

contact = contact.Contact("123456789", "John", "Doe")
# print(contact)

dice = dice.Dice("123456789", "🎲")
# print(dice)

location = location.Location(100, 100)
# print(location)

message = message.Message(
    message_id=123456789,
    date=123456789,
    from_user=user,
    sender_chat=chat,
    chat=chat,
    forward_from=user,
    text="Hello, World!",
    audio=audio,
    document=document,
    photo=[photo_size],
    video=video,
    sticker=photo_size,
    caption="Hello, World!",
    contact=contact,
    dice=dice,
    location=location,
)
# print(message)