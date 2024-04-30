import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    # Налаштування вікна
    window = turtle.Screen()
    window.bgcolor("white")
    
    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0) 

    # Вхідні дані користувача   
    recursion_level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    size = 300  # Довжина кожної сторони сніжинки

    # Початкове положення
    t.up()
    t.goto(-size / 2, size / 3)
    t.down()
    
    # Малювання сніжинки з рекурсією
    for _ in range(3):
        koch_snowflake(t, recursion_level, size)
        t.right(120)

    # Завершення роботи
    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    main()


