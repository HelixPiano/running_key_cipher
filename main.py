from matplotlib import pyplot as plt
import lp_text as lp


def main():
    # Plotting starts
    plot_running_key()
    plot_chapters()
    plt.show()


def plot_chapters():
    plt.figure(2)
    plot_section(lp.crosses, "crosses 0-2", 1)
    plot_section(lp.spirals, "spirals 3-7", 2)
    plot_section(lp.branches, "branches 8-14", 3)
    plot_section(lp.mobius, "mobius 15-22", 4)
    plot_section(lp.mayfly, "mayfly 23-26", 5)
    plot_section(lp.wingtree, "wing-tree 27-32", 6)
    plot_section(lp.cuneiform, "cuneiform 33-39", 7)
    plot_section(lp.spiral_branches, "spiral-branches 40-53", 8)
    plot_section(lp.hollow, "Hollow 54-55", 9)


def plot_section(input_list, name, subplot_number):
    indices = list(range(29))
    labels = (
        "F", "U", "TH", "O", "R", "C", "G", "W", "H", "N", "I", "J", "EO", "P", "X", "S", "T", "B", "E", "M", "L", "NG",
        "OE", "D", "A", "AE", "Y", "IA", "EA")
    plt.subplot(3, 3, subplot_number)
    plt.xticks(indices, labels)
    plt.title(name)

    statistics = [sum(text_letter == index for text_letter in input_list) / len(input_list) * 100
                  for
                  index in range(29)]
    plt.plot(indices, statistics)
    plt.ylabel("Letter frequency in %")
    plt.xlabel("Letters")
    plt.ylim(1, 6)


def plot_running_key():
    indices = list(range(29))
    labels = (
        "F", "U", "TH", "O", "R", "C", "G", "W", "H", "N", "I", "J", "EO", "P", "X", "S", "T", "B", "E", "M", "L", "NG",
        "OE", "D", "A", "AE", "Y", "IA", "EA")

    statistics_solved_pages = [sum(solved_pages_letter == index for solved_pages_letter in lp.solved_pages) / len(lp.solved_pages) * 100
                               for index in range(29)]

    statistics_bible_pages = [sum(bible_text_letter == index for bible_text_letter in lp.bible_text) / len(lp.bible_text) * 100
                              for index in range(29)]

    combined = [sum(x) % 29 for x in zip(lp.solved_pages, lp.bible_text)]
    statistics_combined = [sum(combined_text_letter == index for combined_text_letter in combined) / len(lp.bible_text) * 100
                           for index in range(29)]

    plt.subplot(1, 3, 1)
    plt.title("Translated solved pages")
    plt.xticks(indices, labels)
    plt.plot(indices, statistics_solved_pages)
    plt.ylabel("Letter frequency in %")
    plt.xlabel("Letters")
    plt.ylim(0, 12)

    plt.subplot(1, 3, 2)
    plt.xticks(indices, labels)
    plt.title("Bible")
    plt.plot(indices, statistics_bible_pages)
    plt.ylabel("Letter frequency in %")
    plt.xlabel("Letters")
    plt.ylim(0, 12)

    plt.subplot(1, 3, 3)
    plt.xticks(indices, labels)
    plt.title("Running key cipher")
    plt.plot(indices, statistics_combined)
    plt.ylabel("Letter frequency in %")
    plt.xlabel("Letters")
    plt.ylim(0, 4)


if __name__ == "__main__":
    main()
