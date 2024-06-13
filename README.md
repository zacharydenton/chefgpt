# chefgpt

This project demonstrates the setup and usage of a personalized AI chef using
OpenAI's API to create a unique and interactive cooking assistant.

## Prerequisites

- Python 3.6 or later
- A virtual environment (`venv`) set up and activated
- Environment variable `OPENAI_API_KEY` set to your OpenAI API key

## Usage

```console
$ pip install -r requirements.txt
$ python main.py
```

## Examples

### Suggesting a dish based on ingredients

```
How can I help you today? I can suggest dishes based on ingredients, provide recipes for a given dish, and critique recipes that you provide.
basil, parmesan, pine nuts
I'm thinking of a dish based on the ingredients you specified.
### Dish Name: Basil Pesto with Homemade Trofie Pasta

#### Recipe:

##### Ingredients:
- 2 cups fresh basil leaves
- 1/2 cup grated Parmesan cheese
- 1/3 cup pine nuts
- 2 garlic cloves
- 1/2 cup extra-virgin olive oil
- Salt, to taste
- Black pepper, to taste
- 250g (about 2 cups) Trofie pasta (or any other pasta of your choice)

##### Instructions:

1. **Prepare the Pesto:**
    - In a food processor, combine the fresh basil leaves, grated Parmesan cheese, pine nuts, and garlic cloves.
    - Pulse until all the ingredients are finely chopped.
    - Slowly add the extra-virgin olive oil while continuing to pulse until you achieve a smooth consistency.
    - Season with salt and black pepper to taste. Set aside.

2. **Cook the Pasta:**
    - Bring a large pot of salted water to a boil.
    - Add the Trofie pasta and cook according to the package directions until al dente.
    - Reserve about 1 cup of the pasta cooking water before draining the pasta.

3. **Combine Pasta and Pesto:**
    - In a large mixing bowl, combine the cooked Trofie pasta with the basil pesto.
    - Toss gently to coat the pasta evenly with the pesto sauce.
    - If the sauce is too thick, add a bit of the reserved pasta cooking water until you reach the desired consistency.

4. **Serve:**
    - Plate the basil pesto pasta, garnishing with additional grated Parmesan cheese and a few whole pine nuts for extra texture.
    - Drizzle a little extra-virgin olive oil over the top for an added touch of richness.

Enjoy this simple yet exquisite dish that beautifully highlights the flavors of fresh basil, Parmesan cheese, and pine nuts. Buon appetito!
```

### Providing a recipe for a given dish

```
How can I help you today? I can suggest dishes based on ingredients, provide recipes for a given dish, and critique recipes that you provide.
stock
I'm thinking of a recipe for the dish you specified.
Ah, stock! The very soul of the kitchen, the essence that brings depth and character to our dishes. Let me share with you my approach to making a beautifully rich and flavorful stock that forms the foundation for countless gastronomic creations. We'll create a versatile chicken stock, but with a twist of artistry and local love.

### Ingredients:
- 1.5 kg (3.3 lbs) of organic, free-range chicken bones (preferably a mix of carcasses, wings, and necks for depth of flavor)
- 2 medium onions, peeled and quartered
- 2 carrots, peeled and roughly chopped
- 2 celery stalks, roughly chopped
- 1 head of garlic, halved crosswise
- 1 leek, white part only, thoroughly cleaned and roughly chopped
- 1 ripe tomato, halved
- A small bundle of fresh thyme
- 2-3 sprigs of fresh rosemary
- 2 bay leaves
- 10-12 whole black peppercorns
- A small handful of flat-leaf parsley, including stems
- 4 liters (about 1 gallon) of cold water
- Sea salt to season

### Instructions:

1. **Prepare the Bones:**
   Let's do this with love and precision. Rinse the chicken bones under cold running water to remove any impurities or blood. This will help ensure a clear stock.

2. **Roasting for Depth:**
   Preheat the oven to 200°C (390°F). Arrange the bones in a single layer on a roasting pan. Roast for about 30 minutes, turning halfway through, until they are a deep golden brown. This will caramelize the bones, adding incredible depth and complexity to your stock.

3. **Sweat the Vegetables:**
   While the bones are roasting, take a large, heavy-bottomed stockpot and place it over medium heat. Add a little olive oil for that Italian touch of love. Sweat the onions, carrots, celery, garlic, leek, and tomato. Your kitchen should be filled with the beautiful aroma of these vegetables. Cook them just until they start to soften and release their flavors, about 5-7 minutes.

4. **Building the Stock:**
   Once the bones are beautifully roasted, transfer them to your stockpot. Make sure to scrape in all those delicious browned bits from the roasting pan – they are packed with flavor!

5. **Adding Aromatics and Water:**
   Add the thyme, rosemary, bay leaves, peppercorns, and parsley to the pot. Carefully pour in the cold water, ensuring the bones and vegetables are fully submerged. Using cold water is key; it helps extract flavors more slowly and thoroughly.

6. **Simmering with Patience:**
   Bring the pot to a gentle simmer over medium heat. As the stock reaches a simmer, impurities and foam will rise to the surface. Skim these off diligently with a ladle or spoon. Do not let the stock boil, as boiling can make it cloudy.

7. **Consistency and Clarity:**
   Lower the heat to maintain a gentle simmer. Partially cover the pot and let it cook for at least 4 hours, preferably 6-8 hours. The longer it simmers, the richer and more intense the flavor. Check occasionally to ensure the stock remains at a steady simmer and continue skimming as needed.

8. **Straining the Stock:**
   After simmering to perfection, carefully strain the stock through a fine-mesh sieve lined with cheesecloth into a clean pot or container. Discard the solids – they have given all their love and essence to the stock.

9. **Final Adjustments:**
   Let the stock cool and then refrigerate it. Once chilled, any fat will rise to the top and solidify. Skim off this fat; you want a clear, beautiful stock. Season with sea salt to taste, but remember, keeping it lightly salted gives you more control over seasoning future dishes.

10. **Storing the Gold:**
    Divide the stock into portions and store in airtight containers. It can be kept in the refrigerator for up to 5 days or frozen for 3 months. When frozen, this stock is like having a golden gem in your kitchen, ready to elevate any dish.
With this stock, you hold the key to transforming simple dishes into masterpieces, nourishing both body and soul. Buon appetito!
```

### Critiquing a recipe

```
How can I help you today? I can suggest dishes based on ingredients, provide recipes for a given dish, and critique recipes that you provide.
pasta with meat sauce: 99 cent dried spaghetti from walmart, ground beef, canned crushed tomatoes, italian seasoning
I'm going to tell you what I think about your recipe.
Ah, pasta with meat sauce—a timeless classic that bridges the gap between simplicity and satisfaction. Let's delve into the strengths and potential improvements for this dish, aligning it with the principles of Italian culinary tradition and a more elevated gastronomic experience.

### Ingredients Evaluation:
- **99 Cent Dried Spaghetti from Walmart**: While there's no shame in using budget-friendly pasta, the choice of pasta can drastically impact the dish. Higher-quality pasta brands often use better wheat and have a texture that holds sauce well. Look for brands that use durum wheat semolina and have been bronze-die extruded, which gives the pasta a rougher texture for the sauce to cling to.
- **Ground Beef**: Ground beef is a solid choice, but consider using a mix of beef, pork, and veal to add depth of flavor and complexity. This combination is often found in traditional Italian ragù.
- **Canned Crushed Tomatoes**: These are perfectly acceptable but opt for San Marzano tomatoes if you can. They have a richer, sweeter flavor that can elevate your sauce.
- **Italian Seasoning**: While convenient, using fresh herbs like basil, oregano, and a touch of thyme can make a significant difference. Fresh herbs provide more vibrant and distinct flavors compared to dried mixes.

### Preparation Methods:
1. **Cooking the Pasta**: Ensure the pasta is cooked al dente. This means it should have a slight bite to it, providing a textural contrast to the sauce. Remember to salt the water generously—it should taste like the sea.
2. **Browning the Meat**: Start by browning the ground meats. This process develops a deeper, caramelized flavor. Do not rush this step; allow the meat to achieve a dark, golden crust.
3. **Building the Sauce**: After browning the meat, remove it from the pan and sauté finely chopped onion, carrot, and celery (soffritto) in the rendered fat. This base adds a wonderful sweetness and complexity to your sauce.
4. **Deglazing**: Consider deglazing the pan with a splash of red wine before adding the crushed tomatoes. The wine will add acidity and depth, balancing the richness of the meat.
5. **Simmering**: Allow the sauce to simmer gently for at least an hour. This extended cooking time will meld the flavors beautifully and thicken the sauce naturally.

### Flavor Balance and Harmony:
- **Seasoning**: Taste as you go! Adjust salt and pepper levels gradually. Freshly cracked black pepper can add a lovely kick.
- **Acidity**: Tomatoes bring acidity, but a small dash of balsamic vinegar or a spoonful of sugar can help balance out the acidity if it's too sharp.
- **Herbs**: Add some fresh basil leaves towards the end of cooking for a burst of freshness. Consider a sprinkle of fresh parsley just before serving to brighten the dish.
- **Umami**: For an extra layer of umami, a touch of anchovy paste or a grated Parmesan rind simmered in the sauce can add a deep, savory note.

### Additional Tips:
- **Serving**: When you drain the pasta, reserve a cup of the starchy cooking water. This can be mixed back into the pasta and sauce to achieve the perfect consistency.
- **Finishing Touches**: Off the heat, toss the pasta in the sauce for a minute or two so it absorbs the flavors. Grate fresh Parmigiano-Reggiano over the top before serving—its nutty, salty character ties the whole dish together brilliantly.

By making these adjustments, you can transform a simple pasta with meat sauce into something truly exceptional. Cooking, to me, is about honoring tradition and elevating it with care and creativity. Buon appetito!
```
