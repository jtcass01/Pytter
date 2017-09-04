from API import API
from Tasks import Tasks

class Pytter(object):
    def __init__(self):
        self.twitter = API()
        self.tasks = Tasks()

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
            '0': self.tasks.quit,
            '1': self.tasks.store_tweet,
            '2': self.tasks.start_server,
            '3': self.tasks.analyze
            }

        function = switch.get(task, "invalid input.")

        return function()

def main():
    test_pytter = Pytter()
    while True:
        test_pytter.display_menu()

if __name__ == '__main__':
    main()