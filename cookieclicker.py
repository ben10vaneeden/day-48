import time

from game_stats import Game

game_playing = True
timeout_5_min = time.time() + 60 * 5  # 5 minutes from now
timeout_5_sec = time.time() + 10  # 5 seconds from now
time_start = time.time()
count = 0
game = Game()

while time.time() < timeout_5_min:
    game.big_cookie.click()

    if time.time() >= timeout_5_sec:
        game.get_money()
        game.get_upgrade_prices()
        game.buy_upgrade()
        game.get_cps()
        timeout_5_sec = time.time() + 5
        print(f"CPS:{game.cps.text}")
        print(f"CPS:{game.cps_amount}")

game.driver.close()  # Closes the tab which was opened earlier
game.driver.quit()  # Quits the entire browser.
