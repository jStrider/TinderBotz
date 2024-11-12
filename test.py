class GPTHelper:
    def generate_pickup_line(self, name, bio):
        # Implement the logic to generate a pickup line using name and bio
        # This is just a placeholder implementation
        return f"Hey {name}, I hear you're an {bio}!"

# Example usage in the main function
if __name__ == '__main__':
    helper = GPTHelper()
    name = "Marie"
    bio = "amante des aventures en plein air"
    pickup_line = helper.generate_pickup_line(name, bio)
    print(pickup_line)