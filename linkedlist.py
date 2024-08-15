
class Book:
    def __init__(self, title):
        self.title = title
        self.book_below = None  # equivalent to .next

# StackOfBooks represents a Linked List, with Books for Nodes
class StackOfBooks:
    def __init__(self):
        self.top_of_stack = None # in our linked list, this is our .head

    def find_book(self, title_to_find): # get_node()
        current_book = self.top_of_stack
        # check through all books for title
        while current_book is not None:
            if current_book.title == title_to_find:
                return current_book
            current_book = current_book.book_below
        return None

    def add_book_to_bottom(self, new_title): # append()
        new_book = Book(new_title)
        # check for head-- if none, it's the first book!
        if self.top_of_stack == None:
            self.top_of_stack = new_book
            return
        # else: check for next until there is None, then add our book!
        current_book = self.top_of_stack
        while current_book.book_below is not None:
            current_book = current_book.book_below
        current_book.book_below = new_book

    def insert_book_below(self, new_title, title_above): # insert()
        # check that book to insert below exists
        book_above = self.find_book(title_above)
        if book_above == None:
            print(f"{title_above} is not in this stack!")
        # insert new book and set .book_below properties appropriately
        else:
            new_book = Book(new_title)
            new_book.book_below = book_above.book_below
            book_above.book_below = new_book

    def remove_book(self, title_to_remove): # remove()
        # check for empty stack
        if self.top_of_stack == None:
            print("There are no books in this stack!")
            return
        # handle removing head
        if self.top_of_stack.title == title_to_remove:
            self.top_of_stack = self.top_of_stack.book_below
            return
        # search the stack for the book to remove
        current_book = self.top_of_stack
        while current_book.book_below is not None:
            if current_book.book_below.title == title_to_remove:
                current_book.book_below = current_book.book_below.book_below
                return
            current_book = current_book.book_below
        # the entire stack was search through and the book was not found:
        print(f"{title_to_remove} is not in this stack!")


    def view_all_books(self): # traversal
        # check for head
        if self.top_of_stack == None:
            print("There are no books in this stack!")
            return
        # iterate through all books, printing them out
        current_book = self.top_of_stack
        print()
        while current_book is not None:
            print(' ' + ('-'*len(current_book.title)) + ('-'*10) )
            if current_book == self.top_of_stack:
                print(f"||  | {current_book.title} |  || <-- Top of Stack")
            else:
                print(f"||  | {current_book.title} |  ||")
            current_book = current_book.book_below
        print()

# testing the linked list
books_holding_up_my_coffee_table = StackOfBooks()
# books_holding_up_my_coffee_table.remove_book("Harry Potter 5")
# books_holding_up_my_coffee_table.insert_book_below("Harry Potter 5", "Dictionary")
books_holding_up_my_coffee_table.add_book_to_bottom("Dictionary")
books_holding_up_my_coffee_table.add_book_to_bottom("Encyclopedia M")
books_holding_up_my_coffee_table.insert_book_below("Harry Potter 5", "Dictionary")
books_holding_up_my_coffee_table.insert_book_below("Encyclopedia L", "Harry Potter 5")
books_holding_up_my_coffee_table.remove_book("Harry Potter 5")
# books_holding_up_my_coffee_table.remove_book("Dictionary")
books_holding_up_my_coffee_table.view_all_books()



# Implementing a Doubly Linked List in Python

class YouTubeVideo:
    def __init__(self, title, channel, duration):
        self.title = title
        self.channel = channel
        self.duration = duration

    def __str__(self):
        return f'"{self.title}" | {self.channel} | [{self.duration}]'

class Node:
    def __init__(self, video):
        self.video = video
        self.prev_video = None
        self.next_video = None

class YouTubePlaylist:
    def __init__(self, name):
        self.name = name
        self.playlist_start = None
        self.current_video = None

    # adds video to end of playlist
    def add_video(self, new_video):
        new_node = Node(new_video)
        # check for head; if none, this is our first video
        if self.playlist_start is None:
            self.playlist_start = new_node
        else:
        # iterate through list until we find the end; then add the new video
            node = self.playlist_start
            while node.next_video:
                node = node.next_video
            node.next_video = new_node
            new_node.prev_video = node

    # get node by value of video title
    def get_node(self, video_to_find):
        node = self.playlist_start
        # check through all nodes for video title
        while node:
            if node.video.title == video_to_find:
                return node
            node = node.next_video
        # if not found
        return None

    # inserts video after specified video
    def insert_video(self, new_video, video_before_insert):
        # if video_before_insert is set to None, insert at beginning of list
        if video_before_insert is None:
            new_node = Node(new_video)
            new_node.next_video = self.playlist_start
            if new_node.next_video:
                new_node.next_video.prev_video = new_node
            self.playlist_start = new_node
            return
        # check if insertion point is in playlist
        node_before_insert = self.get_node(video_before_insert)
        if node_before_insert is None:
            print(f'{video_before_insert} is not in playlist "{self.name}"')
        else:
            # add new node at insertion point, setging all .next and .prev values appropriately
            new_node = Node(new_video)
            new_node.next_video = node_before_insert.next_video
            new_node.prev_video = node_before_insert
            node_before_insert.next_video = new_node
            if new_node.next_video:
                new_node.next_video.prev_video = new_node

    # deletion of node
    def remove_video(self, video_to_remove):
        # check if playlist is empty
        if self.playlist_start is None:
            print(f'Playlist "{self.name}" is empty!')
            return
        # handle removing first video
        if self.playlist_start.video.title == video_to_remove:
            self.playlist_start = self.playlist_start.next_video
            return
        # search the rest of the playlist for video_to_remove
        node = self.playlist_start
        while node:
            # if video is found, adjust pointers to remove video from list
            if node.video.title == video_to_remove:
                if node.prev_video:
                    node.prev_video.next_video = node.next_video
                if node.next_video:
                    node.next_video.prev_video = node.prev_video
                return
            node = node.next_video
        # entire playlist was searched but video was not found
        print(f'{video_to_remove} was not found in playlist "{self.name}"')

    # traversal
    def display_all_videos(self):
        # check for empty playlist
        if self.playlist_start is None:
            print(f'There are videos in playlist "{self.name}"')
        # iterate through playlist, printing all videos
        node = self.playlist_start
        print(f"\nPlaylist: {self.name}")
        while node:
            if node == self.playlist_start:
                print(f"{node.video}    << playlist_start")
            else:
                print(f"{node.video}")
            node = node.next_video
        print()

    def play_next(self):
        # start playing at beginning of playlist
        if self.current_video is None:
            self.current_video = self.playlist_start
        else:
            # play the next video
            self.current_video = self.current_video.next_video
        # if a video exist, play that video!
        if self.current_video:
            print(f'Now Playing... "{self.current_video.video.title}"')
        else:
            print(f'You have reached the end of the "{self.name}" playlist.')

    def play_prev(self):
        # cannot go back from beginning of playlilst
        if self.current_video is None:
            print("At the start of the playist. Cannot go back.")
        else:
            # play pervious video
            self.current_video = self.current_video.prev_video
            if self.current_video:
                print(f'Playing Previous... "{self.current_video.video.title}"')
            else:
                print(f'You are back at the beginning of the "{self.name}" playlist.')

# testing the playlist
watch_later = YouTubePlaylist("Watch Later")
watch_later.add_video(YouTubeVideo("Three Artists Try Drawing Pokemon from Memory", "Drawfee Show", "17:07"))
watch_later.add_video(YouTubeVideo("Just a relaxing walk around Los Santos", "DayDream Gaming", "5:05:45"))
watch_later.insert_video(YouTubeVideo("Dog of Wisdom", "Joe", "1:01"), "Three Artists Try Drawing Pokemon from Memory")
watch_later.insert_video(YouTubeVideo("hello there...", "JablinskiGames", "0:11"), None)
watch_later.insert_video(YouTubeVideo("Why the STAR WARS Prequels are ACTUALLY about George Lucas’s Divorce - Video Essay", 
                                      "ScreenCrush", "22:29"), "Dog of Wisdom")
watch_later.display_all_videos()
watch_later.remove_video("Dog of Wisdom")
watch_later.display_all_videos()

watch_later.play_next()
watch_later.play_next()
watch_later.play_next()
watch_later.play_next()
watch_later.play_next()
print()

watch_later.play_next()
watch_later.play_next()
watch_later.play_next()
watch_later.play_next()
watch_later.play_prev()
watch_later.play_prev()
watch_later.play_prev()
watch_later.play_prev()
