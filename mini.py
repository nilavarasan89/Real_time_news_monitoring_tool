# Real-Time News Sentiment Monitoring Tool

positive_words = [
    "good","great","excellent","positive","growth","profit","benefit",
    "success","improve","happy","strong","win","increase"
]

negative_words = [
    "bad","poor","loss","negative","decline","fall","crisis",
    "weak","drop","fail","problem","decrease"
]




def analyze_sentiment(news):
    
    words = news.lower().split()
    
    positive_count = 0
    negative_count = 0
    
    for word in words:
        
        if word in positive_words:
            positive_count = positive_count + 1
        
        elif word in negative_words:
            negative_count = negative_count + 1
    
    
    if positive_count > negative_count:
        return "Positive"
    
    elif negative_count > positive_count:
        return "Negative"
    
    else:
        return "Neutral"


def add_news():
    
    news = input("Enter News Headline : ")
    
    file = open("news_data.txt","a")
    
    file.write(news + "\n")
    
    file.close()
    
    print("News Saved Successfully\n")


def read_news():
    
    file = open("news_data.txt","r")
    
    data = file.readlines()
    
    file.close()
    
    return data


def analyze_all_news():
    
    news_list = read_news()
    
    results = []
    
    for news in news_list:
        
        sentiment = analyze_sentiment(news)
        
        results.append((news.strip(), sentiment))
    
    
    print("\nNews Sentiment Report")
    print("--------------------------")
    
    for item in results:
        print("News :", item[0])
        print("Sentiment :", item[1])
        print()


def sentiment_summary():
    
    news_list = read_news()
    
    positive = 0
    negative = 0
    neutral = 0
    
    for news in news_list:
        
        result = analyze_sentiment(news)
        
        if result == "Positive":
            positive = positive + 1
        
        elif result == "Negative":
            negative = negative + 1
        
        else:
            neutral = neutral + 1
    
    
    print("\nSummary")
    print("----------------")
    print("Positive News :", positive)
    print("Negative News :", negative)
    print("Neutral News :", neutral)



while True:
    
    print("\nReal-Time News Sentiment Monitoring Tool")
    print("---------------------------------------")
    print("1. Add News")
    print("2. View News Sentiment")
    print("3. Sentiment Summary")
    print("4. Exit")
    
    
    choice = input("Enter your choice : ")
    
    
    if choice == "1":
        add_news()
    
    elif choice == "2":
        analyze_all_news()
    
    elif choice == "3":
        sentiment_summary()
    
    elif choice == "4":
        print("Program Ended")
        break
    
    else:
        print("Invalid Choice")