import sys

from transformers import pipeline


def main():
    sentences = sys.argv[1:]
    if len(sentences) == 0:
        sys.exit(1, "Missing arguments: 1 or more sentences required to run sentiment analysis")

    classifier = pipeline("sentiment-analysis")
    results = classifier(sentences)

    print(results)


if __name__ == "__main__":
    main()
