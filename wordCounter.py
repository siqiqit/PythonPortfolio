#Siqi Tang
#Period 3
#Word Counter
#February 11, 2025

#Initialize

#Functions

def word_counter(text):

#Initialization
    count = 0
    txt = text

#Splitting the words into lists
    wordList = txt.split()

#printing list
    print(txt)
#Counting items in list
    for i in range(len(wordList)):
        count = count + 1

#Printing word count
    print("Word Count: " + str(count))

#Main
word_counter("Lorem ipsum dolor sit amet. Non sint quod ea voluptas molestias aut rerum voluptatibus eum repudiandae minima a doloribus deserunt et modi mollitia. Et temporibus ipsam qui illo libero eos optio voluptate est dolor ullam ad accusantium quos quo quidem dolorem. Sed esse unde quo fugit molestiae qui ipsum perspiciatis ab corporis molestiae. Et asperiores praesentium et odit illo et velit pariatur vel expedita excepturi qui officiis sapiente et iusto autem! Vel amet excepturi nam amet accusantium sit quisquam eius ex voluptatibus omnis est facere dicta in dolor consectetur. Nam dolores velit non culpa eius sit fuga consequatur ea aliquid quia ut sunt internos? Ut cupiditate maxime sed minima modi vel neque voluptate est magnam Quis ut dolorem similique sed quam neque in nisi ducimus. Qui laborum voluptatem At molestiae modi eum vero temporibus 33 rerum beatae eos sunt velit et adipisci unde.")
