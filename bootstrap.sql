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
    recipe_id integer NOT NULL,
    user_id integer,
    recipe_name character varying(200),
    ingredients text,
    description text,
    direction text,
    image_url character varying(200)
);


ALTER TABLE public.recipes OWNER TO darlaluangrath;

--
-- Name: recipes_recipe_id_seq; Type: SEQUENCE; Schema: public; Owner: darlaluangrath
--

CREATE SEQUENCE public.recipes_recipe_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipes_recipe_id_seq OWNER TO darlaluangrath;

--
-- Name: recipes_recipe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: darlaluangrath
--

ALTER SEQUENCE public.recipes_recipe_id_seq OWNED BY public.recipes.recipe_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: darlaluangrath
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    email character varying(100),
    name character varying(25),
    password character varying(20)
);


ALTER TABLE public.users OWNER TO darlaluangrath;

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: darlaluangrath
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO darlaluangrath;

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: darlaluangrath
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: favorites id; Type: DEFAULT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites ALTER COLUMN id SET DEFAULT nextval('public.favorites_id_seq'::regclass);


--
-- Name: recipes recipe_id; Type: DEFAULT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.recipes ALTER COLUMN recipe_id SET DEFAULT nextval('public.recipes_recipe_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: favorites; Type: TABLE DATA; Schema: public; Owner: darlaluangrath
--

COPY public.favorites (id, recipe_id, user_id, time_created) FROM stdin;
1	665257	1	2023-01-04 16:53:13.633114
\.


--
-- Data for Name: recipes; Type: TABLE DATA; Schema: public; Owner: darlaluangrath
--

COPY public.recipes (recipe_id, user_id, recipe_name, ingredients, description, direction, image_url) FROM stdin;
658509	\N	Roasted Broccoli with Lemon and Garlic	5 cups Organic Broccoli Florets<br>2 teaspoons Extra Virgin Olive Oil<br>1 clove of garlic, or more<br>½ teaspoons Ground Black Pepper<br>½ teaspoons Lemon Juice<br>1/2 teaspoon salt<br>	Roasted Broccoli with Lemon and Garlic might be just the side dish you are searching for. One serving contains <b>58 calories</b>, <b>3g of protein</b>, and <b>2g of fat</b>. For <b>30 cents per serving</b>, this recipe <b>covers 14%</b> of your daily requirements of vitamins and minerals. Not a lot of people made this recipe, and 4 would say it hit the spot. Head to the store and pick up salt, ground pepper, garlic, and a few other things to make it today. From preparation to the plate, this recipe takes roughly <b>45 minutes</b>. It is a good option if you're following a <b>caveman, gluten free, primal, and whole 30</b> diet. All things considered, we decided this recipe <b>deserves a spoonacular score of 94%</b>. This score is great. Try <a href="https://spoonacular.com/recipes/roasted-broccoli-with-garlic-and-lemon-29354">Roasted Broccoli With Garlic And Lemon</a>, <a href="https://spoonacular.com/recipes/roasted-broccoli-with-garlic-and-lemon-706892">Roasted Broccoli with Garlic and Lemon</a>, and <a href="https://spoonacular.com/recipes/roasted-garlic-lemon-broccoli-110090">Roasted Garlic Lemon Broccoli</a> for similar recipes.	<ol><li>Preheat the oven to 400 degrees F</li><li>In a large bowl, add broccoli florets, olive oil, salt, pepper and garlic. Spread the broccoli out in an even layer on a baking sheet.</li><li>Bake in the preheated oven until broccoli is tender enough to pierce the stems with a fork, 15 to 20 minutes.</li><li>Remove and place in a bowl, toss with lemon juice.</li></ol>	https://spoonacular.com/recipeImages/658509-556x370.jpg
643150	\N	Fluffy frittata with spinach	8 eggs, separated<br>2 cloves garlic, finely chopped<br>½ tsp ground pepper, freshly ground<br>3/4 teaspoon nutmeg<br>1 ½ Tbs olive oil<br>1/3 cup parmesan<br>½ cup ricotta cheese<br>1/4 teaspoon salt<br>140 g fresh spinach, cleaned, blanched, well-drained and chopped<br>140g frozen chopped spinach, thawed and wrung dry or<br>	Fluffy frittata with spinach might be just the main course you are searching for. This gluten free, primal, and ketogenic recipe serves 4 and costs <b>$1.55 per serving</b>. One serving contains <b>279 calories</b>, <b>20g of protein</b>, and <b>20g of fat</b>. A mixture of spinach, olive oil, spinach, and a handful of other ingredients are all it takes to make this recipe so tasty. To use up the eggs you could follow this main course with the <a href="https://spoonacular.com/recipes/rose-levy-beranbaums-chocolate-tomato-cake-with-mystery-ganache-27408">Rose Levy Beranbaum's Chocolate Tomato Cake with Mystery Ganache</a> as a dessert. Only a few people made this recipe, and 7 would say it hit the spot. From preparation to the plate, this recipe takes roughly <b>45 minutes</b>. All things considered, we decided this recipe <b>deserves a spoonacular score of 74%</b>. This score is pretty good. Try <a href="https://spoonacular.com/recipes/fluffy-bacon-cheese-frittata-147451">Fluffy Bacon-Cheese Frittata</a>, <a href="https://spoonacular.com/recipes/fluffy-gluten-free-spinach-cheese-biscuits-682018">Fluffy Gluten Free Spinach Cheese Biscuits</a>, and <a href="https://spoonacular.com/recipes/fluffy-light-yummy-spinach-blue-cheese-souffle-427654">Fluffy, Light & Yummy: Spinach & Blue Cheese Souffle</a> for similar recipes.	<ol><li>In a medium oven-proof skillet heat the olive oil, add the garlic and cook until softened.</li><li>In a glass or metal bowl, beat the egg whites until stiff peaks form. In another bowl, beat the egg yolks and stir in the spinach and ricotta cheese; season with the salt, pepper and nutmeg. Fold in the egg whites.</li><li>Pour the mixture into the hot skillet and cook over medium heat until just set around the edges, about 2 minutes.</li><li>Transfer the frittata to the oven and bake at 200C until golden and fluffy, about 15 minutes.</li><li>Sprinkle the parmesan all over the top and bake for 2 minutes.</li><li>Cut into wedges and serve immediately.</li></ol>	https://spoonacular.com/recipeImages/643150-556x370.jpg
715438	\N	Mexican Casserole	4 boneless chicken breasts<br>2 cups shredded Monterrey Jack<br>1 (10oz) cream of chicken soup<br>1 (10oz) cream of mushroom soup<br>1 onion, finely chopped<br>1 cup uncooked rice<br>1 cup salsa<br>2 cups shredded Cheddar Cheese<br>	The recipe Mexican Casserole could satisfy your Mexican craving in around <b>1 hour and 5 minutes</b>. This recipe serves 6 and costs $1.97 per serving. This main course has <b>494 calories</b>, <b>33g of protein</b>, and <b>19g of fat</b> per serving. It can be enjoyed any time, but it is especially good for <b>Autumn</b>. 503 people have made this recipe and would make it again. Head to the store and pick up salsa, monterrey jack, cream of chicken soup, and a few other things to make it today. To use up the salsa you could follow this main course with the <a href="https://spoonacular.com/recipes/dessert-strawberry-salsa-553911">Dessert Strawberry Salsa</a> as a dessert. It is a good option if you're following a <b>gluten free</b> diet. All things considered, we decided this recipe <b>deserves a spoonacular score of 79%</b>. This score is solid. Try <a href="https://spoonacular.com/recipes/mexican-cornbread-casserole-make-a-mexican-casserole-dinner-that-is-easy-to-make-and-reheats-well-600366">Mexican Cornbread Casserole – make a Mexican casserole dinner that is easy to make, and reheats well</a>, <a href="https://spoonacular.com/recipes/mexican-casserole-162857">Mexican Casserole</a>, and <a href="https://spoonacular.com/recipes/mexican-casserole-513196">Mexican Casserole</a> for similar recipes.	Take a large pot and ring water to a boil. When finished, place you chicken breasts in to boil for 20 minutes or until cooked. Take a smaller pan and cook rice as directed. Allow both rice and chicken time to cool when once fully cooked. Heat over to 350 degrees. Take cooled chicken breasts and shred, or cut into bite size pieces. Add into a large mixing bowl. Stir in cooked rice, 2 cups of Monterrey Jack cheese, and 1 cup of Cheddar. Stir in both soups, chopped onion, and salsa.Take a 9 x 13 baking dish and coat with non stick spray. Place mixture into the 9 x 13 dish and cover with the remaining cup of cheddar cheese. Bake for 40 minutes. Allow to cool before serving.	https://spoonacular.com/recipeImages/715438-556x370.jpg
665257	\N	Whole Grain Pumpkin Bread	2 teaspoons baking soda<br>1 1/2 cups firmly packed light brown sugar<br>16 ounces can pumpkin (Libby's)<br>2 teaspoons cinnamon<br>2 eggs, well beaten<br>2 cups flour<br>1 teaspoon ground cloves<br>1/2 cup molasses<br>1 teaspoon nutmeg<br>cup oat bran<br>1 cup oil or butter<br>1/4 cup pecans, finely chopped<br>1/2 teaspoon salt<br>cup wheat bran<br>cup wheat germ<br>1/2 cup whole wheat flour<br>	Whole Grain Pumpkin Bread is a <b>dairy free and vegetarian</b> morn meal. One serving contains <b>182 calories</b>, <b>5g of protein</b>, and <b>3g of fat</b>. This recipe serves 24 and costs 42 cents per serving. A couple people made this recipe, and 13 would say it hit the spot. From preparation to the plate, this recipe takes roughly <b>45 minutes</b>. A mixture of eggs, salt, ground cloves, and a handful of other ingredients are all it takes to make this recipe so scrumptious. All things considered, we decided this recipe <b>deserves a spoonacular score of 68%</b>. This score is pretty good. Similar recipes include <a href="https://spoonacular.com/recipes/multi-grain-pumpkin-cranberry-bread-66662">Multi-Grain Pumpkin Cranberry Bread</a>, <a href="https://spoonacular.com/recipes/grain-free-pumpkin-pie-496345">Grain Free Pumpkin Pie</a>, and <a href="https://spoonacular.com/recipes/whole-grain-pumpkin-scones-311551">Whole-Grain Pumpkin Scones</a>.	<ol><li>Preheat oven to 375 degrees. Grease 2 loaf pans. Beat oil, brown sugar and molasses until well blended. Blend in egg and pumpkin. Stir flours, brans, wheat germ, soda, cinnamon, cloves, nutmeg and salt into mixture just until moistened. Fold in nuts. Fill pans and bake about 1 hour, until pick comes out clean. Cool on rack. Better if served the day after cooking.</li></ol>	https://spoonacular.com/recipeImages/665257-556x370.jpg
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: darlaluangrath
--

COPY public.users (user_id, email, name, password) FROM stdin;
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
-- Name: recipes_recipe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: darlaluangrath
--

SELECT pg_catalog.setval('public.recipes_recipe_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: darlaluangrath
--

SELECT pg_catalog.setval('public.users_user_id_seq', 11, true);


--
-- Name: favorites favorites_pkey; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_pkey PRIMARY KEY (id);


--
-- Name: recipes recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_pkey PRIMARY KEY (recipe_id);


--
-- Name: recipes recipes_recipe_name_key; Type: CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_recipe_name_key UNIQUE (recipe_name);


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
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: favorites favorites_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(recipe_id);


--
-- Name: favorites favorites_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.favorites
    ADD CONSTRAINT favorites_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- Name: recipes recipes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: darlaluangrath
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

