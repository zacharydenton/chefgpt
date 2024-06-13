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
"Pesto alla Genovese with Parmesan Crumble"
```

### Providing a recipe for a given dish

```
How can I help you today? I can suggest dishes based on ingredients, provide recipes for a given dish, and critique recipes that you provide.
Pesto alla Genovese with Parmesan Crumble                                                                                                                                                                                                       I'm thinking of a recipe for the dish you specified.
Ah, Pesto alla Genovese! This is a dish that sings with the essence of Liguria, a true symphony of basil and olive oil, elevated by the crunch of Parmesan crumble. Let us dive into this beautiful dance of flavors together.

### Ingredients:

**For the Pesto:**
- 100g fresh basil leaves, washed and dried
- 60g Parmigiano-Reggiano, freshly grated
- 60g Pecorino Romano, freshly grated
- 30g pine nuts
- 2 garlic cloves
- 150ml extra-virgin olive oil, the elixir of the gods
- A pinch of coarse sea salt

**For the Parmesan Crumble:**
- 80g Parmigiano-Reggiano, finely grated
- 50g all-purpose flour
- 50g cold unsalted butter, cut into small cubes
- A pinch of salt

### Preparation:

#### 1. Preparing the Pesto alla Genovese:

1. **Toast the Pine Nuts:**
   Gently toast the pine nuts in a dry skillet over medium heat until they are golden brown and release their natural oils. This step is quick, so keep an eye on them to avoid burning. Once done, set them aside to cool.

2. **Pounding the Basil:**
   In a mortar and pestle, combine the garlic cloves with a pinch of coarse sea salt. The salt acts as an abrasive, breaking down the garlic. Add the basil leaves in small batches, grinding them into a fine paste. The slow, circular motion allows the oils to release, giving the pesto its vibrant flavor and aroma.

3. **Adding Cheese and Nuts:**
   Add the toasted pine nuts and continue to grind until they are fully incorporated. Gradually mix in the grated Parmigiano-Reggiano and Pecorino Romano.

4. **Emulsifying with Olive Oil:**
   Slowly drizzle in the extra-virgin olive oil while stirring continuously. The goal is to create a creamy, harmonious blend that sings with each stir.

#### 2. Preparing the Parmesan Crumble:

1. **Mixing the Ingredients:**
   In a bowl, combine the grated Parmigiano-Reggiano, all-purpose flour, and a pinch of salt. Add the cold, cubed butter and use your fingertips to rub the butter into the dry ingredients until the mixture resembles coarse breadcrumbs.

2. **Baking:**
   Preheat your oven to 180°C (350°F). Spread the mixture in an even layer on a baking sheet lined with parchment paper. Bake for about 10-12 minutes, or until the crumble is golden and crisp. Allow it to cool, then break it into small, delightful pieces.

#### 3. Putting it all Together:

1. **Cook the Pasta:**
   Prepare your favorite pasta (traditionally, trofie or trenette) according to the package instructions. Remember, al dente is the way to go, to ensure each bite is perfect.

2. **Combining Pesto and Pasta:**
   Reserve a cup of pasta water before draining the pasta. Return the pasta to the pot and add the pesto. Stir gently, adding a bit of the reserved pasta water to achieve a silky-smooth consistency.

3. **Serving:**
   Plate the pasta and sprinkle generously with the Parmesan crumble. The contrast between the creamy pesto and the crunchy crumble is a textural symphony that is sure to delight the senses.

### Final Touch:

Garnish with a few fresh basil leaves and a drizzle of your finest extra-virgin olive oil. As you take your first bite, close your eyes and let the flavors transport you to the sun-drenched coasts of Liguria, where tradition and innovation dance in perfect harmony.

Buon appetito!
```

### Critiquing a recipe

```
How can I help you today? I can suggest dishes based on ingredients, provide recipes for a given dish, and critique recipes that you provide.
### Ingredients: **For the Pesto:** - 100g fresh basil leaves, washed and dried - 60g Parmigiano-Reggiano, freshly grated - 60g Pecorino Romano, freshly grated - 30g pine nuts - 2 garlic cloves - 150ml extra-virgin olive oil, the elixir of the gods - A pinch of coarse sea salt **For the Parmesan Crumble:** - 80g Parmigiano-Reggiano, finely grated - 50g all-purpose flour - 50g cold unsalted butter, cut into small cubes - A pinch of salt ### Preparation: #### 1. Preparing the Pesto alla Genovese: 1. **Toast the Pine Nuts:** Gently toast the pine nuts in a dry skillet over medium heat until they are golden brown and release their natural oils. This step is quick, so keep an eye on them to avoid burning. Once done, set them aside to cool. 2. **Pounding the Basil:** In a mortar and pestle, combine the garlic cloves with a pinch of coarse sea salt. The salt acts as an abrasive, breaking down the garlic. Add the basil leaves in small batches, grinding them into a fine paste. The slow, circular motion allows the oils to release, giving the pesto its vibrant flavor and aroma. 3. **Adding Cheese and Nuts:** Add the toasted pine nuts and continue to grind until they are fully incorporated. Gradually mix in the grated Parmigiano-Reggiano and Pecorino Romano. 4. **Emulsifying with Olive Oil:** Slowly drizzle in the extra-virgin olive oil while stirring continuously. The goal is to create a creamy, harmonious blend that sings with each stir. #### 2. Preparing the Parmesan Crumble: 1. **Mixing the Ingredients:** In a bowl, combine the grated Parmigiano-Reggiano, all-purpose flour, and a pinch of salt. Add the cold, cubed butter and use your fingertips to rub the butter into the dry ingredients until the mixture resembles coarse breadcrumbs. 2. **Baking:** Preheat your oven to 180°C (350°F). Spread the mixture in an even layer on a baking sheet lined with parchment paper. Bake for about 10-12 minutes, or until the crumble is golden and crisp. Allow it to cool, then break it into small, delightful pieces. #### 3. Putting it all Together: 1. **Cook the Pasta:** Prepare your favorite pasta (traditionally, trofie or trenette) according to the package instructions. Remember, al dente is the way to go, to ensure each bite is perfect. 2. **Combining Pesto and Pasta:** Reserve a cup of pasta water before draining the pasta. Return the pasta to the pot and add the pesto. Stir gently, adding a bit of the reserved pasta water to achieve a silky-smooth consistency. 3. **Serving:** Plate the pasta and sprinkle generously with the Parmesan crumble. The contrast between the creamy pesto and the crunchy crumble is a textural symphony that is sure to delight the senses. ### Final Touch: Garnish with a few fresh basil leaves and a drizzle of your finest extra-virgin olive oil. As you take your first bite, close your eyes and let the flavors transport you to the sun-drenched coasts of Liguria, where tradition and innovation dance in perfect harmony.
I'm going to tell you what I think about your recipe.
This recipe for Pesto alla Genovese with Parmesan Crumble is beautifully crafted and shows a deep respect for traditional Ligurian cuisine while incorporating some delightful innovations. Let’s delve into a detailed critique and offer suggestions for further enhancement.

### Ingredients:
**For the Pesto:**
- The selection of ingredients here is authentic and well-balanced. The use of both Parmigiano-Reggiano and Pecorino Romano creates a beautiful harmony of flavors, combining the nutty sweetness of Parmigiano with the sharpness of Pecorino.

- Toasting the pine nuts adds a layer of complexity, enhancing their natural flavor. This is an excellent touch.

**For the Parmesan Crumble:**
- The crumble is an innovative addition that adds a wonderful textural contrast to the dish—something that is often missing in traditional pesto pasta.

### Preparation:

#### 1. Preparing the Pesto alla Genovese:
1. **Toast the Pine Nuts:**
   - Perfect. The toasting step is important to bring out the nuttiness. A suggestion here: consider adding a touch of lemon zest just before removing them from the heat. This can enhance the freshness of the pesto.

2. **Pounding the Basil:**
   - Using a mortar and pestle is traditional and brings out the best in basil. The slow method really enriches the fragrance and taste.
   - When adding basil leaves in batches, ensure you pound each batch until smooth, as residual large basil leaves can cause inconsistency in the final texture.

3. **Adding Cheese and Nuts:**
   - The method is sound. For consistency, you might pulse the nuts lightly before adding them to the mortar for easier mixing.

4. **Emulsifying with Olive Oil:**
   - Drizzling in the olive oil slowly while stirring ensures a smooth, creamy pesto. Another tip: refrigerate the mortar and pestle before use to keep the pesto cool, preventing oxidation and preserving its vibrant green color longer.

#### 2. Preparing the Parmesan Crumble:
1. **Mixing the Ingredients:**
   - The use of cold butter is key to achieving the right crumbly texture. Consider adding a touch of fresh thyme or rosemary to the mix for an aromatic hint.

2. **Baking:**
   - The temperature and timing here are spot-on. After baking, you might toss the crumble with a little extra grated Parmigiano for added flavor intensity.

#### 3. Putting it all Together:
1. **Cook the Pasta:**
   - Al dente is absolutely the way to go. Undercook by about a minute and finish cooking in the sauce for optimal flavor absorption.

2. **Combining Pesto and Pasta:**
   - Adding reserved pasta water is crucial for achieving that perfect, silky consistency. However, be cautious with the amount to avoid diluting the pesto.

3. **Serving:**
   - Beautifully described. For a finer presentation touch, you might sprinkle some lightly toasted pine nuts and perhaps a few shavings of Parmigiano over the plated dish.

### Final Touch:
- The garnish of fresh basil leaves and a drizzle of extra-virgin olive oil will not only enhance presentation but also elevate the aromatic elements just before serving.

### Final Suggestions:
- If you want to innovate further, consider making basil oil by lightly blending basil with olive oil and letting it sit. Use this basil-infused oil to drizzle over the dish before serving.
- For a stronger umami punch, try incorporating a little anchovy fillet into the pesto during the pounding stage. It melts away, leaving behind an incredible depth of flavor without being fishy.

Overall, this recipe is a beautiful blend of tradition and modernity. It respects the essence of Pesto alla Genovese while adding a unique twist with the Parmesan crumble. Buon appetito!
```
