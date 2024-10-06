import turtle

# Функція побудови однієї сторони кривої Коха
def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

# Функція малювання сніжинки Коха
def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Малюємо всі сторони сніжинки
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    try:
        order = int(input("Введіть рівень рекурсії: "))
        if order < 0:
            print("Рівень рекурсії повинен бути додатним числом.")
            return
        draw_koch_snowflake(order)
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")

if __name__ == "__main__":
    main()
