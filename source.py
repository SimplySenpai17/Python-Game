import curses
import random

def setup_screen():
    scr = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    scr.keypad(True)
    return scr

def end_game():
    curses.nocbreak()
    curses.echo()
    curses.endwin()

def show_game_over(scr, score):
    scr.clear()
    scr.addstr(5, 10, "Game Over", curses.A_BOLD)
    scr.addstr(6, 10, f"Score: {score}")
    scr.refresh()
    scr.getch()

def game(scr):
    screen_height, screen_width = scr.getmaxyx()
    player_pos = [screen_height - 2, screen_width // 2]
    player_char = "A"
    enemy_char = "V"
    bullet_char = "^"
    enemies = [[1, random.randint(0, screen_width - 1)]]
    bullets = []
    score = 0
    frame_count = 0
    scr.timeout(100)
    key = None

    while key != ord('q'):
        scr.clear()
        scr.addch(player_pos[0], player_pos[1], player_char)

        for enemy in enemies:
            scr.addch(enemy[0], enemy[1], enemy_char)

        for bullet in bullets:
            scr.addch(bullet[0], bullet[1], bullet_char)

        scr.refresh()
        key = scr.getch()

        if key == curses.KEY_LEFT and player_pos[1] > 0:
            player_pos[1] -= 1
        if key == curses.KEY_RIGHT and player_pos[1] < screen_width - 1:
            player_pos[1] += 1
        if key == ord(' '):
            bullets.append([player_pos[0] - 1, player_pos[1]])

        for i in range(len(bullets)):
            bullets[i][0] -= 1

        bullets = [bullet for bullet in bullets if bullet[0] > 0]

        if frame_count % 15 == 0:
            for enemy in enemies:
                enemy[0] += 1

        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet[0] == enemy[0] and bullet[1] == enemy[1]:
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    break

        for enemy in enemies:
            if enemy[0] >= screen_height - 1:
                show_game_over(scr, score)
                return

        if frame_count % 30 == 0:
            enemies.append([1, random.randint(0, screen_width - 1)])

        frame_count += 1
        scr.addstr(0, 0, f"Score: {score}")

def main():
    scr = setup_screen()
    try:
        game(scr)
    finally:
        end_game()

if __name__ == "__main__":
    main()
