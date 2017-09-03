from API import API
from Tasks import Tasks

class Pytter(object):
    def __init__(self):
        self.twitter = API()

    def display_menu(self):
        print("===== Pytter Menu =====")
        print("1 ) Store a new tweet for later use.")
        print("2 ) Start twitter server for automatic tweets.")
        print("3 ) Perform analysis.")
        print("0 ) Quit.")

        response = input("What would you like to do?\t")
        assert int(response) < 4 and int(response) >= 0
        self.perform_task(response)

    def perform_task(self, task):
        switch = {
            '0': Tasks.quit,
            '1': Tasks.store_tweet,
            '2': Tasks.start_server,
            '3': Tasks.analyze
            }

        function = switch.get(task, "invalid input.")

        return function()

def main():
    test_pytter = Pytter()
    while True:
        test_pytter.display_menu()

if __name__ == '__main__':
    main()