
def greeter_bot():
    name = yield "Enter your name"

    while True:
        name = yield f"Hello, {name}!"


bot = greeter_bot()

print(next(bot))           
print(bot.send("Keti"))    
print(bot.send("Saba"))    
print(bot.send("Nutsa"))  