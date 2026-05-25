def count_chars_excluding_spaces(s: str) -> int:
	"""Return the number of characters in s excluding space characters (' ')."""
	return len(s.replace(' ', ''))


def main() -> None:
	user = input("Enter a string: ")
	count = count_chars_excluding_spaces(user)
	if count == 0:
		# covers empty input or input that only contains space characters
		print("The string contains no characters when spaces are excluded.")
	else:
		print("Number of characters (excluding spaces):", count)


if __name__ == "__main__":
	main()


