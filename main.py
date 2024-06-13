#!/usr/bin/env python
from pick import pick
from openai import OpenAI

PERSONALITIES = {
    "zacharydenton": """
You are Massimo Bottura, an acclaimed Italian chef known for your innovative
and artistic approach to traditional Italian cuisine.

You own the three-Michelin-starred restaurant Osteria Francescana in Modena,
Italy, which has been named the best restaurant in the world multiple times.

You are known for your creativity, passion for storytelling through food, and
your dedication to using high-quality, locally-sourced ingredients.

You believe in preserving and reinventing Italian culinary traditions, and you
approach cooking as both an art and a science.

You are warm, personable, and always eager to share your deep knowledge of
Italian cuisine with others, while inspiring them to appreciate the beauty and
complexity of food.
""",
    # Add your personality here
}

MODEL = "gpt-4o"


def select_personality(personalities):
    keys = list(personalities.keys())
    selected = pick(keys, "Select a chef:")
    return personalities[selected[0]].strip()


def determine_task(client, prompt):
    messages = [
        {
            "role": "system",
            "content": (
                "Your client will interact with you in three main ways: by asking for dish suggestions based on ingredients, requesting detailed recipes for specific dishes, or providing recipes for critique and suggestions for improvement. "
                "Categorize each user input into one of these four categories: 'suggest_dish', 'suggest_recipe', 'critique_recipe', or 'unknown' if the input does not fit any of the specified categories."
            ),
        },
        {
            "role": "system",
            "content": (
                "If the client provides one or more ingredients, respond with 'suggest_dish'."
            ),
        },
        {
            "role": "system",
            "content": (
                "If the client provides the name of a dish, respond with 'suggest_recipe'. For example, if the input is \"lasagna\", then the response should be 'suggest_recipe'."
            ),
        },
        {
            "role": "system",
            "content": (
                "If the client provides a recipe, respond with 'critique_recipe'."
            ),
        },
        {
            "role": "system",
            "content": (
                "If the client input does not fit into any of the above categories, respond with 'unknown'."
            ),
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    try:
        return response.choices[0].message.content
    except:
        return "unknown"


def stream_response(client, messages):
    stream = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True,
    )

    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")


def suggest_dish(client, personality, prompt):
    print("I'm thinking of a dish based on the ingredients you specified.")

    messages = [
        {
            "role": "system",
            "content": personality,
        },
        {
            "role": "system",
            "content": "Your task is to suggest a dish based on the ingredients provided by the user. Do not provide the recipe at this stage; only suggest a dish name that can be made with the given ingredients.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    stream_response(client, messages)


def suggest_recipe(client, personality, prompt):
    print("I'm thinking of a recipe for the dish you specified.")

    messages = [
        {
            "role": "system",
            "content": personality,
        },
        {
            "role": "system",
            "content": "Your task is to provide a detailed recipe for the specified dish. The recipe should include a list of ingredients, precise measurements, and step-by-step preparation instructions. Ensure the recipe reflects your unique personality.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    stream_response(client, messages)


def critique_recipe(client, personality, prompt):
    print("I'm going to tell you what I think about your recipe.")

    messages = [
        {
            "role": "system",
            "content": personality,
        },
        {
            "role": "system",
            "content": "Your task is to provide a detailed critique of a specified recipe. Evaluate the recipe based on the ingredients used, the preparation methods, and the overall balance and harmony of flavors. Offer constructive feedback, suggest improvements or adjustments, and provide any tips or techniques that could enhance the dish. Ensure your critique is respectful, insightful, and reflects your expertise and unique culinary perspective. Focus on what works well in the recipe, as well as areas that could be improved. Suggest specific changes or enhancements to help the user achieve a superior result, inspired by your own cooking philosophy and experience.",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    stream_response(client, messages)


def main():
    client = OpenAI()
    personality = select_personality(PERSONALITIES)

    while True:
        prompt = input(
            "How can I help you today? I can suggest dishes based on ingredients, provide recipes for a given dish, and critique recipes that you provide.\n"
        )
        task = determine_task(client, prompt)
        if task == "suggest_dish":
            return suggest_dish(client, personality, prompt)
        elif task == "suggest_recipe":
            return suggest_recipe(client, personality, prompt)
        elif task == "critique_recipe":
            return critique_recipe(client, personality, prompt)
        else:
            print("I'm sorry, I didn't understand that.")


if __name__ == "__main__":
    main()
