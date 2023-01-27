--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Homebrew)
-- Dumped by pg_dump version 14.5 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: favorites; Type: TABLE; Schema: public; Owner: darlaluangrath
--

CREATE TABLE public.favorites (
    id integer NOT NULL,
    recipe_id integer,
    user_id integer,
    time_created timestamp without time zone NOT NULL
);


ALTER TABLE public.favorites OWNER TO darlaluangrath;

--
-- Name: favorites_id_seq; Type: SEQUENCE; Schema: public; Owner: darlaluangrath
--

CREATE SEQUENCE public.favorites_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.favorites_id_seq OWNER TO darlaluangrath;

--
-- Name: favorites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: darlaluangrath
--

ALTER SEQUENCE public.favorites_id_seq OWNED BY public.favorites.id;


--
-- Name: recipes; Type: TABLE; Schema: public; Owner: darlaluangrath
--

CREATE TABLE public.recipes (
    id integer NOT NULL,
    title character varying(200),
    ingredients text,
    summary text,
    instructions text,
    image_url character varying(200)
);


ALTER TABLE public.recipes OWNER TO darlaluangrath;

--
-- Name: recipes_id_seq; Type: SEQUENCE; Schema: public; Owner: darlaluangrath
--

CREATE SEQUENCE public.recipes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipes_id_seq OWNER TO darlaluangrath;

--
-- Name: recipes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: darlaluangrath
--

ALTER SEQUENCE public.recipes_id_seq OWNED BY public.recipes.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: darlaluangrath
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(100),
    name character varying(25),
    password character varying(20)
);


ALTER TABLE public.users OWNER TO darlaluangrath;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: darlaluangrath
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO darlaluangrath;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: darlaluangrath
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: favorites id; Type: DEFAULT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites ALTER COLUMN id SET DEFAULT nextval('public.favorites_id_seq'::regclass);


--
-- Name: recipes id; Type: DEFAULT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.recipes ALTER COLUMN id SET DEFAULT nextval('public.recipes_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: favorites; Type: TABLE DATA; Schema: public; Owner: darlaluangrath
--

COPY public.favorites (id, recipe_id, user_id, time_created) FROM stdin;
1	665257	1	2023-01-06 11:44:05.919813
\.


--
-- Data for Name: recipes; Type: TABLE DATA; Schema: public; Owner: darlaluangrath
--

COPY public.recipes (id, title, ingredients, summary, instructions, image_url) FROM stdin;
636641	Cabbage and sausages in beer	200ml beer<br>6 tablespoons Butter or margarine, divided<br>400g green cabbage, halved lengthwise, cut into two-finger-width wedges<br>1 small Onion, (diced)<br>Pepper to taste<br>150g potatoes, cut into chunks<br>1 teaspoon Salt<br>200g smoked sausages, cut into thumb-length pieces<br>½ Tbs sugar<br>	Cabbage and sausages in beer might be just the side dish you are searching for. Watching your figure? This gluten free recipe has <b>506 calories</b>, <b>12g of protein</b>, and <b>41g of fat</b> per serving. This recipe serves 3 and costs $1.65 per serving. 15 people have made this recipe and would make it again. From preparation to the plate, this recipe takes around <b>45 minutes</b>. It can be enjoyed any time, but it is especially good for <b>Father's Day</b>. If you have cabbage, butter, sugar, and a few other ingredients on hand, you can make it. All things considered, we decided this recipe <b>deserves a spoonacular score of 65%</b>. This score is solid. Try <a href="https://spoonacular.com/recipes/beer-cheese-mac-and-sausages-160934">Beer-Cheese Mac and Sausages</a>, <a href="https://spoonacular.com/recipes/roasted-sausages-with-beer-braised-onions-40014">Roasted Sausages with Beer-braised Onions</a>, and <a href="https://spoonacular.com/recipes/beer-braised-sausages-with-warm-potato-salad-107415">Beer-Braised Sausages with Warm Potato Salad</a> for similar recipes.	<ol><li>Melt the butter in a large pan over medium-low heat, add the onion, sugar and salt and cook them, stirring frequently, until the onion is golden, about 5-8 minutes.</li><li>Stir in the beer, scraping up any bits from the bottom of the pan.</li><li>Add the sausages, cabbage and potatoes and simmer, covered, stirring occasionally, for 20 minutes or until the vegetables are tender.</li><li>Serve the sausages and veggies in big bowls with plenty of the cooking liquid, sprinkled with freshly cracked pepper.</li></ol>	https://spoonacular.com/recipeImages/636641-556x370.jpg
716334	Plantain Toffee Balls	2 tablespoons of butter<br>1 tablespoon of coconut flakes<br>4 tablespoons of coconut milk<br>3 tablespoons of flour<br>1 finger of plantain<br>3.5 tablespoons of sugar<br>1 teaspoon of vanilla<br>4 tablespoons of water<br>	Plantain Toffee Balls might be just the side dish you are searching for. One serving contains <b>413 calories</b>, <b>3g of protein</b>, and <b>20g of fat</b>. This vegetarian recipe serves 2 and costs <b>77 cents per serving</b>. 14 people were impressed by this recipe. From preparation to the plate, this recipe takes about <b>45 minutes</b>. A mixture of butter, vanilla, coconut milk, and a handful of other ingredients are all it takes to make this recipe so delicious. All things considered, we decided this recipe <b>deserves a spoonacular score of 31%</b>. This score is rather bad. Try <a href="https://spoonacular.com/recipes/juj-green-plantain-and-cheese-balls-629173">Jujú (Green Plantain and Cheese Balls)</a>, <a href="https://spoonacular.com/recipes/ripe-plantain-balls-buuelos-de-pltano-maduro-226285">Ripe Plantain Balls (Buñuelos de Plátano Maduro)</a>, and <a href="https://spoonacular.com/recipes/cacao-coconut-plantain-rice-balls-with-pepitas-563942">Cacao-Coconut Plantain Rice Balls with Pepitas</a> for similar recipes.	Peel and mash your plantain till soft. Mix it with the flour, form mini balls and place in the oven to bake for about 20-25 minutes. Please note the plantain mix will still be moist so use a spoon to help form the balls if you are having difficulty with that. Make sure to drizzle oil on the baking sheet so it does not stick to the sheet when it begins to caramelize. If you do not have an oven you can choose to fry the plantain balls as well. I have not tried the frying method but make sure to dab off the excess oil from the plantain.In a separate pot, on very low heat, melt the butter and pour in the sugar, vanilla, milk and water and stir. Leave it on very low heat throughout. Stir once in a while and if you have a candy thermometer, it is ready at 240F. If you do not, the toffee base is ready when it turns light brown like a caramel colour.Dip the plantain balls and swirl and place on a plate to cool. While its still warm, sprinkle your toppings on it. In this case, my toppings were coconut flakes. Serve when it’s cool.	https://spoonacular.com/recipeImages/716334-556x370.jpg
645530	Green Tea Fruit Medley Smoothie	1 cup water<br>3 Bigelow® Green Tea Bags*<br>1 cup fresh berries, choose from raspberries, blueberries,or strawberries<br>¼ cup pineapple juice<br>½ cup vanilla yogurt<br>½ cup ice cubes<br>	Green Tea Fruit Medley Smoothie could be just the <b>gluten free, lacto ovo vegetarian, and primal</b> recipe you've been looking for. This recipe serves 4. This breakfast has <b>54 calories</b>, <b>2g of protein</b>, and <b>1g of fat</b> per serving. For <b>77 cents per serving</b>, this recipe <b>covers 3%</b> of your daily requirements of vitamins and minerals. A mixture of pineapple juice, tea bags, berries, and a handful of other ingredients are all it takes to make this recipe so scrumptious. 60 people were impressed by this recipe. From preparation to the plate, this recipe takes around <b>around 45 minutes</b>. It is brought to you by Foodista. All things considered, we decided this recipe <b>deserves a spoonacular score of 37%</b>. This score is not so awesome. If you like this recipe, take a look at these similar recipes: <a href="https://spoonacular.com/recipes/green-tea-fruit-smoothie-marianos-health-key-system-536257">Green Tea Fruit Smoothie – Mariano’s health key System</a>, <a href="https://spoonacular.com/recipes/a-beginner-green-tea-green-smoothie-473896">A Beginner Green Tea Green Smoothie</a>, and <a href="https://spoonacular.com/recipes/green-tea-smoothie-717810">Green Tea Smoothie</a>.	Prepare tea by steeping 3 Bigelow Green tea bags in 1 cup of boiling water for 5 minutes. Squeeze out bags and discard.\nCombine tea and remaining ingredients in blender and blend until smooth.	https://spoonacular.com/recipeImages/645530-556x370.jpg
665257	Whole Grain Pumpkin Bread	2 teaspoons baking soda<br>1 1/2 cups firmly packed light brown sugar<br>16 ounces can pumpkin (Libby's)<br>2 teaspoons cinnamon<br>2 eggs, well beaten<br>2 cups flour<br>1 teaspoon ground cloves<br>1/2 cup molasses<br>1 teaspoon nutmeg<br>cup oat bran<br>1 cup oil or butter<br>1/4 cup pecans, finely chopped<br>1/2 teaspoon salt<br>cup wheat bran<br>cup wheat germ<br>1/2 cup whole wheat flour<br>	Whole Grain Pumpkin Bread is a <b>dairy free and vegetarian</b> morn meal. One serving contains <b>182 calories</b>, <b>5g of protein</b>, and <b>3g of fat</b>. This recipe serves 24 and costs 42 cents per serving. A couple people made this recipe, and 13 would say it hit the spot. From preparation to the plate, this recipe takes roughly <b>45 minutes</b>. A mixture of eggs, salt, ground cloves, and a handful of other ingredients are all it takes to make this recipe so scrumptious. All things considered, we decided this recipe <b>deserves a spoonacular score of 68%</b>. This score is pretty good. Similar recipes include <a href="https://spoonacular.com/recipes/multi-grain-pumpkin-cranberry-bread-66662">Multi-Grain Pumpkin Cranberry Bread</a>, <a href="https://spoonacular.com/recipes/grain-free-pumpkin-pie-496345">Grain Free Pumpkin Pie</a>, and <a href="https://spoonacular.com/recipes/whole-grain-pumpkin-scones-311551">Whole-Grain Pumpkin Scones</a>.	<ol><li>Preheat oven to 375 degrees. Grease 2 loaf pans. Beat oil, brown sugar and molasses until well blended. Blend in egg and pumpkin. Stir flours, brans, wheat germ, soda, cinnamon, cloves, nutmeg and salt into mixture just until moistened. Fold in nuts. Fill pans and bake about 1 hour, until pick comes out clean. Cool on rack. Better if served the day after cooking.</li></ol>	https://spoonacular.com/recipeImages/665257-556x370.jpg
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: darlaluangrath
--

COPY public.users (id, email, name, password) FROM stdin;
1	darla@email.com	Darla	qwerty
2	mtizzard0@sina.com.cn	Marrilee	Ko0N59Ayi
3	dbrandin1@icio.us	Daphene	S7YWlR6z
4	rrowler2@youtube.com	Rudd	vf6mhWirHFb
5	kmccowen3@usnews.com	Kennith	qRdg4GKq3MV
6	gmonahan4@opera.com	Guilbert	VP0Telt
7	boreagan5@t.co	Barron	JpnupOoKCokz
8	fgyurkovics6@netscape.com	Flss	McJmfRYDC6D
9	nhaslum7@feedburner.com	Norina	AUPxPJj
10	fmcdougald8@stanford.edu	Ferne	hJp0grwRMxs
11	rbirchett9@example.com	Ramsey	qoOK888j9b
\.


--
-- Name: favorites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: darlaluangrath
--

SELECT pg_catalog.setval('public.favorites_id_seq', 1, true);


--
-- Name: recipes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: darlaluangrath
--

SELECT pg_catalog.setval('public.recipes_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: darlaluangrath
--

SELECT pg_catalog.setval('public.users_id_seq', 11, true);


--
-- Name: favorites favorites_pkey; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_pkey PRIMARY KEY (id);


--
-- Name: favorites favorites_user_id_recipe_id_key; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_user_id_recipe_id_key UNIQUE (user_id, recipe_id);


--
-- Name: recipes recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_pkey PRIMARY KEY (id);


--
-- Name: recipes recipes_title_key; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_title_key UNIQUE (title);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_name_key; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_name_key UNIQUE (name);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: favorites favorites_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: favorites favorites_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

