a = { 
    "Beetroot":"chukandar",
    "Bitter Gourd":"karela",      
    "capsicum":"shimlamirch",
    "cucumber":"khira",
    "pumpkin":"kaddu",
    "cabbage":"pattagobi",
    "brinjal":"bagun",
    "corn":"makka",
    "cauliflower":"fhulgobi",
    "tomato":"tamatar",
    "carrot":"gajar",
    "cluster beans":"gvar fhali",
    "chilli":"mirch",
    "ginger":"adrak",
    "radish":"mulli",
    "coriander leaf":"dhaniya",
    "bengal gram":"chana",
    "green onion":"hari pyaj",
    "lady fingar":"bhindi",
    "turnip":"salgam",
    "mashroom":"kukarmuta",
    "garlic":"lahesun",
    "mustard greens":"sarso ka patta",
    "potato":"allu",
    "sweet potato":"sakarkand",
    "pea":"matar",
    "jack fruit":"kathal",
    "onion":"pyaj",
    "ridgid gourd":"tori",
    "turmeric":"haldi"
 }
print( a.keys())

b=input("write one vagetable name when you want to  see in hindi\n")

# print(a[b])
print(a.get(b))
