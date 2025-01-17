import random

spanish_words = [
    {'English': 'the', 'Spanish': 'el'},
    {'English': 'of', 'Spanish': 'de'},
    {'English': 'that', 'Spanish': 'que'},
    {'English': 'and', 'Spanish': 'y'},
    {'English': 'to', 'Spanish': 'a'},
    {'English': 'in', 'Spanish': 'en'},
    {'English': 'a', 'Spanish': 'un'},
    {'English': 'to be', 'Spanish': 'ser'},
    {'English': 'self', 'Spanish': 'se'},
    {'English': 'no', 'Spanish': 'no'},
    {'English': 'for', 'Spanish': 'por'},
    {'English': 'on', 'Spanish': 'con'},
    {'English': 'his', 'Spanish': 'su'},
    {'English': 'he', 'Spanish': 'él'},
    {'English': 'as', 'Spanish': 'como'},
    {'English': 'I', 'Spanish': 'yo'},
    {'English': 'but', 'Spanish': 'pero'},
    {'English': 'more', 'Spanish': 'más'},
    {'English': 'or', 'Spanish': 'o'},
    {'English': 'when', 'Spanish': 'cuando'},
    {'English': 'very', 'Spanish': 'muy'},
    {'English': 'all', 'Spanish': 'todo'},
    {'English': 'me', 'Spanish': 'me'},
    {'English': 'there is', 'Spanish': 'hay'},
    {'English': 'how', 'Spanish': 'cómo'},
    {'English': 'this', 'Spanish': 'este'},
    {'English': 'what', 'Spanish': 'qué'},
    {'English': 'to know', 'Spanish': 'saber'},
    {'English': 'time', 'Spanish': 'tiempo'},
    {'English': 'one', 'Spanish': 'uno'},
    {'English': 'so', 'Spanish': 'tan'},
    {'English': 'to see', 'Spanish': 'ver'},
    {'English': 'because', 'Spanish': 'porque'},
    {'English': 'to give', 'Spanish': 'dar'},
    {'English': 'only', 'Spanish': 'solo'},
    {'English': 'to want', 'Spanish': 'querer'},
    {'English': 'to come', 'Spanish': 'venir'},
    {'English': 'to use', 'Spanish': 'usar'},
    {'English': 'who', 'Spanish': 'quién'},
    {'English': 'two', 'Spanish': 'dos'},
    {'English': 'to tell', 'Spanish': 'decir'},
    {'English': 'first', 'Spanish': 'primero'},
    {'English': 'new', 'Spanish': 'nuevo'},
    {'English': 'to find', 'Spanish': 'encontrar'},
    {'English': 'thing', 'Spanish': 'cosa'},
    {'English': 'to feel', 'Spanish': 'sentir'},
    {'English': 'people', 'Spanish': 'gente'},
    {'English': 'many', 'Spanish': 'mucho'},
    {'English': 'good', 'Spanish': 'bueno'},
    {'English': 'to think', 'Spanish': 'pensar'},
    {'English': 'some', 'Spanish': 'algunos'},
    {'English': 'to leave', 'Spanish': 'salir'},
    {'English': 'to work', 'Spanish': 'trabajar'},
    {'English': 'now', 'Spanish': 'ahora'},
    {'English': 'always', 'Spanish': 'siempre'},
    {'English': 'life', 'Spanish': 'vida'},
    {'English': 'to speak', 'Spanish': 'hablar'},
    {'English': 'last', 'Spanish': 'último'},
    {'English': 'never', 'Spanish': 'nunca'},
    {'English': 'without', 'Spanish': 'sin'},
    {'English': 'long', 'Spanish': 'largo'},
    {'English': 'same', 'Spanish': 'mismo'},
    {'English': 'to ask', 'Spanish': 'preguntar'},
    {'English': 'to finish', 'Spanish': 'terminar'},
    {'English': 'to follow', 'Spanish': 'seguir'},
    {'English': 'to read', 'Spanish': 'leer'},
    {'English': 'to write', 'Spanish': 'escribir'},
    {'English': 'to listen', 'Spanish': 'escuchar'},
    {'English': 'to open', 'Spanish': 'abrir'},
    {'English': 'to change', 'Spanish': 'cambiar'},
    {'English': 'to begin', 'Spanish': 'empezar'},
    {'English': 'small', 'Spanish': 'pequeño'},
    {'English': 'young', 'Spanish': 'joven'},
    {'English': 'to understand', 'Spanish': 'entender'},
    {'English': 'to pay', 'Spanish': 'pagar'},
    {'English': 'to sleep', 'Spanish': 'dormir'},
    {'English': 'to forget', 'Spanish': 'olvidar'},
    {'English': 'to buy', 'Spanish': 'comprar'},
    {'English': 'to sell', 'Spanish': 'vender'},
    {'English': 'to call', 'Spanish': 'llamar'},
    {'English': 'to listen', 'Spanish': 'oír'},
    {'English': 'truth', 'Spanish': 'verdad'},
    {'English': 'to laugh', 'Spanish': 'reír'},
    {'English': 'to walk', 'Spanish': 'caminar'},
    {'English': 'to enter', 'Spanish': 'entrar'},
    {'English': 'to play', 'Spanish': 'jugar'},
    {'English': 'to wait', 'Spanish': 'esperar'},
    {'English': 'quickly', 'Spanish': 'rápido'},
    {'English': 'beautiful', 'Spanish': 'hermoso'},
    {'English': 'to run', 'Spanish': 'correr'},
    {'English': 'old', 'Spanish': 'viejo'},
    {'English': 'sad', 'Spanish': 'triste'},
    {'English': 'happy', 'Spanish': 'feliz'},
    {'English': 'strong', 'Spanish': 'fuerte'},
    {'English': 'cold', 'Spanish': 'frío'},
    {'English': 'to rain', 'Spanish': 'llover'},
    {'English': 'to love', 'Spanish': 'amar'},
    {'English': 'to die', 'Spanish': 'morir'},
]

german_words= [  {'English': 'the', 'German': 'der'},
    {'English': 'of', 'German': 'von'},
    {'English': 'and', 'German': 'und'},
    {'English': 'to', 'German': 'zu'},
    {'English': 'a', 'German': 'ein'},
    {'English': 'in', 'German': 'in'},
    {'English': 'is', 'German': 'ist'},
    {'English': 'you', 'German': 'du'},
    {'English': 'that', 'German': 'dass'},
    {'English': 'it', 'German': 'es'},
    {'English': 'he', 'German': 'er'},
    {'English': 'was', 'German': 'war'},
    {'English': 'for', 'German': 'für'},
    {'English': 'on', 'German': 'auf'},
    {'English': 'with', 'German': 'mit'},
    {'English': 'as', 'German': 'als'},
    {'English': 'I', 'German': 'ich'},
    {'English': 'his', 'German': 'sein'},
    {'English': 'they', 'German': 'sie'},
    {'English': 'be', 'German': 'sein'},
    {'English': 'at', 'German': 'bei'},
    {'English': 'one', 'German': 'eins'},
    {'English': 'have', 'German': 'haben'},
    {'English': 'this', 'German': 'dies'},
    {'English': 'from', 'German': 'aus'},
    {'English': 'by', 'German': 'bei'},
    {'English': 'hot', 'German': 'heiß'},
    {'English': 'word', 'German': 'Wort'},
    {'English': 'but', 'German': 'aber'},
    {'English': 'what', 'German': 'was'},
    {'English': 'some', 'German': 'einige'},
    {'English': 'we', 'German': 'wir'},
    {'English': 'can', 'German': 'können'},
    {'English': 'out', 'German': 'aus'},
    {'English': 'other', 'German': 'andere'},
    {'English': 'were', 'German': 'waren'},
    {'English': 'all', 'German': 'alle'},
    {'English': 'there', 'German': 'dort'},
    {'English': 'when', 'German': 'wann'},
    {'English': 'up', 'German': 'oben'},
    {'English': 'use', 'German': 'benutzen'},
    {'English': 'your', 'German': 'dein'},
    {'English': 'how', 'German': 'wie'},
    {'English': 'said', 'German': 'sagte'},
    {'English': 'an', 'German': 'ein'},
    {'English': 'each', 'German': 'jede'},
    {'English': 'she', 'German': 'sie'},
    {'English': 'which', 'German': 'welche'},
    {'English': 'do', 'German': 'tun'},
    {'English': 'their', 'German': 'ihre'},
    {'English': 'time', 'German': 'Zeit'},
    {'English': 'if', 'German': 'wenn'},
    {'English': 'will', 'German': 'wird'},
    {'English': 'way', 'German': 'Weg'},
    {'English': 'about', 'German': 'über'},
    {'English': 'many', 'German': 'viele'},
    {'English': 'then', 'German': 'dann'},
    {'English': 'them', 'German': 'sie'},
    {'English': 'write', 'German': 'schreiben'},
    {'English': 'would', 'German': 'würde'},
    {'English': 'like', 'German': 'mögen'},
    {'English': 'so', 'German': 'so'},
    {'English': 'these', 'German': 'diese'},
    {'English': 'her', 'German': 'ihr'},
    {'English': 'long', 'German': 'lang'},
    {'English': 'make', 'German': 'machen'},
    {'English': 'thing', 'German': 'Ding'},
    {'English': 'see', 'German': 'sehen'},
    {'English': 'him', 'German': 'ihn'},
    {'English': 'two', 'German': 'zwei'},
    {'English': 'has', 'German': 'hat'},
    {'English': 'look', 'German': 'sehen'},
    {'English': 'more', 'German': 'mehr'},
    {'English': 'day', 'German': 'Tag'},
    {'English': 'could', 'German': 'konnte'},
    {'English': 'go', 'German': 'gehen'},
    {'English': 'come', 'German': 'kommen'},
    {'English': 'did', 'German': 'tat'},
    {'English': 'number', 'German': 'Nummer'},
    {'English': 'sound', 'German': 'Klang'},
    {'English': 'no', 'German': 'nein'},
    {'English': 'most', 'German': 'meisten'},
    {'English': 'people', 'German': 'Leute'},
    {'English': 'my', 'German': 'mein'},
    {'English': 'over', 'German': 'über'},
    {'English': 'know', 'German': 'wissen'},
    {'English': 'water', 'German': 'Wasser'},
    {'English': 'than', 'German': 'als'},
    {'English': 'call', 'German': 'rufen'},
    {'English': 'first', 'German': 'erste'},
    {'English': 'who', 'German': 'wer'},
    {'English': 'may', 'German': 'dürfen'},
    {'English': 'down', 'German': 'unten'},
    {'English': 'side', 'German': 'Seite'},
    {'English': 'been', 'German': 'gewesen'},
    {'English': 'now', 'German': 'jetzt'},
    {'English': 'find', 'German': 'finden'},
    {'English': 'head', 'German': 'Kopf'},
    {'English': 'stand', 'German': 'stehen'},
    {'English': 'own', 'German': 'eigen'},
    {'English': 'page', 'German': 'Seite'},
]

french_word =[ {'English': 'the', 'French': 'le'},
    {'English': 'of', 'French': 'de'},
    {'English': 'and', 'French': 'et'},
    {'English': 'to', 'French': 'à'},
    {'English': 'a', 'French': 'un'},
    {'English': 'in', 'French': 'dans'},
    {'English': 'is', 'French': 'est'},
    {'English': 'you', 'French': 'tu'},
    {'English': 'that', 'French': 'que'},
    {'English': 'it', 'French': 'il'},
    {'English': 'he', 'French': 'il'},
    {'English': 'was', 'French': 'était'},
    {'English': 'for', 'French': 'pour'},
    {'English': 'on', 'French': 'sur'},
    {'English': 'with', 'French': 'avec'},
    {'English': 'as', 'French': 'comme'},
    {'English': 'I', 'French': 'je'},
    {'English': 'his', 'French': 'son'},
    {'English': 'they', 'French': 'ils'},
    {'English': 'be', 'French': 'être'},
    {'English': 'at', 'French': 'à'},
    {'English': 'one', 'French': 'un'},
    {'English': 'have', 'French': 'avoir'},
    {'English': 'this', 'French': 'ce'},
    {'English': 'from', 'French': 'de'},
    {'English': 'by', 'French': 'par'},
    {'English': 'hot', 'French': 'chaud'},
    {'English': 'word', 'French': 'mot'},
    {'English': 'but', 'French': 'mais'},
    {'English': 'what', 'French': 'quoi'},
    {'English': 'some', 'French': 'quelques'},
    {'English': 'we', 'French': 'nous'},
    {'English': 'can', 'French': 'pouvoir'},
    {'English': 'out', 'French': 'dehors'},
    {'English': 'other', 'French': 'autre'},
    {'English': 'were', 'French': 'étaient'},
    {'English': 'all', 'French': 'tout'},
    {'English': 'there', 'French': 'là'},
    {'English': 'when', 'French': 'quand'},
    {'English': 'up', 'French': 'en haut'},
    {'English': 'use', 'French': 'utiliser'},
    {'English': 'your', 'French': 'ton'},
    {'English': 'how', 'French': 'comment'},
    {'English': 'said', 'French': 'dit'},
    {'English': 'an', 'French': 'un'},
    {'English': 'each', 'French': 'chaque'},
    {'English': 'she', 'French': 'elle'},
    {'English': 'which', 'French': 'quel'},
    {'English': 'do', 'French': 'faire'},
    {'English': 'their', 'French': 'leur'},
    {'English': 'time', 'French': 'temps'},
    {'English': 'if', 'French': 'si'},
    {'English': 'will', 'French': 'volonté'},
    {'English': 'way', 'French': 'chemin'},
    {'English': 'about', 'French': 'à propos de'},
    {'English': 'many', 'French': 'beaucoup'},
    {'English': 'then', 'French': 'puis'},
    {'English': 'them', 'French': 'eux'},
    {'English': 'write', 'French': 'écrire'},
    {'English': 'would', 'French': 'voudrais'},
    {'English': 'like', 'French': 'aimer'},
    {'English': 'so', 'French': 'tellement'},
    {'English': 'these', 'French': 'ces'},
    {'English': 'her', 'French': 'sa'},
    {'English': 'long', 'French': 'long'},
    {'English': 'make', 'French': 'faire'},
    {'English': 'thing', 'French': 'chose'},
    {'English': 'see', 'French': 'voir'},
    {'English': 'him', 'French': 'lui'},
    {'English': 'two', 'French': 'deux'},
    {'English': 'has', 'French': 'a'},
    {'English': 'look', 'French': 'regarder'},
    {'English': 'more', 'French': 'plus'},
    {'English': 'day', 'French': 'jour'},
    {'English': 'could', 'French': 'pourrait'},
    {'English': 'go', 'French': 'aller'},
    {'English': 'come', 'French': 'venir'},
    {'English': 'did', 'French': 'a fait'},
    {'English': 'number', 'French': 'nombre'},
    {'English': 'sound', 'French': 'son'},
    {'English': 'no', 'French': 'non'},
    {'English': 'most', 'French': 'la plupart'},
    {'English': 'people', 'French': 'gens'},
    {'English': 'my', 'French': 'mon'},
    {'English': 'over', 'French': 'sur'},
    {'English': 'know', 'French': 'savoir'},
    {'English': 'water', 'French': 'eau'},
    {'English': 'than', 'French': 'que'},
    {'English': 'call', 'French': 'appeler'},
    {'English': 'first', 'French': 'premier'},
    {'English': 'who', 'French': 'qui'},
    {'English': 'may', 'French': 'mai'},
    {'English': 'down', 'French': 'en bas'},
    {'English': 'side', 'French': 'côté'},
    {'English': 'been', 'French': 'été'},
    {'English': 'now', 'French': 'maintenant'},
    {'English': 'find', 'French': 'trouver'},
    {'English': 'head', 'French': 'tête'},
    {'English': 'stand', 'French': 'debout'},
    {'English': 'own', 'French': 'propre'},
    {'English': 'page', 'French': 'page'},
]

italian_words= [ {'English': 'the', 'Italian': 'il'},
    {'English': 'of', 'Italian': 'di'},
    {'English': 'and', 'Italian': 'e'},
    {'English': 'to', 'Italian': 'a'},
    {'English': 'a', 'Italian': 'un'},
    {'English': 'in', 'Italian': 'in'},
    {'English': 'is', 'Italian': 'è'},
    {'English': 'you', 'Italian': 'tu'},
    {'English': 'that', 'Italian': 'che'},
    {'English': 'it', 'Italian': 'esso'},
    {'English': 'he', 'Italian': 'lui'},
    {'English': 'was', 'Italian': 'era'},
    {'English': 'for', 'Italian': 'per'},
    {'English': 'on', 'Italian': 'su'},
    {'English': 'with', 'Italian': 'con'},
    {'English': 'as', 'Italian': 'come'},
    {'English': 'I', 'Italian': 'io'},
    {'English': 'his', 'Italian': 'suo'},
    {'English': 'they', 'Italian': 'essi'},
    {'English': 'be', 'Italian': 'essere'},
    {'English': 'at', 'Italian': 'a'},
    {'English': 'one', 'Italian': 'uno'},
    {'English': 'have', 'Italian': 'avere'},
    {'English': 'this', 'Italian': 'questo'},
    {'English': 'from', 'Italian': 'da'},
    {'English': 'by', 'Italian': 'da'},
    {'English': 'hot', 'Italian': 'caldo'},
    {'English': 'word', 'Italian': 'parola'},
    {'English': 'but', 'Italian': 'ma'},
    {'English': 'what', 'Italian': 'cosa'},
    {'English': 'some', 'Italian': 'alcuni'},
    {'English': 'we', 'Italian': 'noi'},
    {'English': 'can', 'Italian': 'potere'},
    {'English': 'out', 'Italian': 'fuori'},
    {'English': 'other', 'Italian': 'altro'},
    {'English': 'were', 'Italian': 'erano'},
    {'English': 'all', 'Italian': 'tutti'},
    {'English': 'there', 'Italian': 'lì'},
    {'English': 'when', 'Italian': 'quando'},
    {'English': 'up', 'Italian': 'su'},
    {'English': 'use', 'Italian': 'usare'},
    {'English': 'your', 'Italian': 'tuo'},
    {'English': 'how', 'Italian': 'come'},
    {'English': 'said', 'Italian': 'ha detto'},
    {'English': 'an', 'Italian': 'un'},
    {'English': 'each', 'Italian': 'ogni'},
    {'English': 'she', 'Italian': 'lei'},
    {'English': 'which', 'Italian': 'quale'},
    {'English': 'do', 'Italian': 'fare'},
    {'English': 'their', 'Italian': 'loro'},
    {'English': 'time', 'Italian': 'tempo'},
    {'English': 'if', 'Italian': 'se'},
    {'English': 'will', 'Italian': 'volontà'},
    {'English': 'way', 'Italian': 'strada'},
    {'English': 'about', 'Italian': 'circa'},
    {'English': 'many', 'Italian': 'molti'},
    {'English': 'then', 'Italian': 'poi'},
    {'English': 'them', 'Italian': 'essi'},
    {'English': 'write', 'Italian': 'scrivere'},
    {'English': 'would', 'Italian': 'vorrebbe'},
    {'English': 'like', 'Italian': 'piacere'},
    {'English': 'so', 'Italian': 'così'},
    {'English': 'these', 'Italian': 'questi'},
    {'English': 'her', 'Italian': 'sua'},
    {'English': 'long', 'Italian': 'lungo'},
    {'English': 'make', 'Italian': 'fare'},
    {'English': 'thing', 'Italian': 'cosa'},
    {'English': 'see', 'Italian': 'vedere'},
    {'English': 'him', 'Italian': 'lui'},
    {'English': 'two', 'Italian': 'due'},
    {'English': 'has', 'Italian': 'ha'},
    {'English': 'look', 'Italian': 'guardare'},
    {'English': 'more', 'Italian': 'più'},
    {'English': 'day', 'Italian': 'giorno'},
    {'English': 'could', 'Italian': 'potrebbe'},
    {'English': 'go', 'Italian': 'andare'},
    {'English': 'come', 'Italian': 'venire'},
    {'English': 'did', 'Italian': 'ha fatto'},
    {'English': 'number', 'Italian': 'numero'},
    {'English': 'sound', 'Italian': 'suono'},
    {'English': 'no', 'Italian': 'no'},
    {'English': 'most', 'Italian': 'la maggior parte'},
    {'English': 'people', 'Italian': 'persone'},
    {'English': 'my', 'Italian': 'mio'},
    {'English': 'over', 'Italian': 'oltre'},
    {'English': 'know', 'Italian': 'sapere'},
    {'English': 'water', 'Italian': 'acqua'},
    {'English': 'than', 'Italian': 'di'},
    {'English': 'call', 'Italian': 'chiamare'},
    {'English': 'first', 'Italian': 'primo'},
    {'English': 'who', 'Italian': 'chi'},
    {'English': 'may', 'Italian': 'maggio'},
    {'English': 'down', 'Italian': 'giù'},
    {'English': 'side', 'Italian': 'lato'},
    {'English': 'been', 'Italian': 'stato'},
    {'English': 'now', 'Italian': 'adesso'},
    {'English': 'find', 'Italian': 'trovare'},
    {'English': 'head', 'Italian': 'testa'},
    {'English': 'stand', 'Italian': 'stare'},
    {'English': 'own', 'Italian': 'proprio'},
    {'English': 'page', 'Italian': 'pagina'},
]

kanji_words=[  {'English': 'one', 'Kanji': '一'},
    {'English': 'two', 'Kanji': '二'},
    {'English': 'three', 'Kanji': '三'},
    {'English': 'four', 'Kanji': '四'},
    {'English': 'five', 'Kanji': '五'},
    {'English': 'six', 'Kanji': '六'},
    {'English': 'seven', 'Kanji': '七'},
    {'English': 'eight', 'Kanji': '八'},
    {'English': 'nine', 'Kanji': '九'},
    {'English': 'ten', 'Kanji': '十'},
    {'English': 'person', 'Kanji': '人'},
    {'English': 'man', 'Kanji': '男'},
    {'English': 'woman', 'Kanji': '女'},
    {'English': 'child', 'Kanji': '子'},
    {'English': 'mountain', 'Kanji': '山'},
    {'English': 'river', 'Kanji': '川'},
    {'English': 'tree', 'Kanji': '木'},
    {'English': 'forest', 'Kanji': '森'},
    {'English': 'sun', 'Kanji': '日'},
    {'English': 'moon', 'Kanji': '月'},
    {'English': 'fire', 'Kanji': '火'},
    {'English': 'water', 'Kanji': '水'},
    {'English': 'earth', 'Kanji': '土'},
    {'English': 'gold', 'Kanji': '金'},
    {'English': 'sky', 'Kanji': '空'},
    {'English': 'rain', 'Kanji': '雨'},
    {'English': 'book', 'Kanji': '本'},
    {'English': 'name', 'Kanji': '名'},
    {'English': 'school', 'Kanji': '校'},
    {'English': 'car', 'Kanji': '車'},
    {'English': 'hand', 'Kanji': '手'},
    {'English': 'eye', 'Kanji': '目'},
    {'English': 'ear', 'Kanji': '耳'},
    {'English': 'mouth', 'Kanji': '口'},
    {'English': 'foot', 'Kanji': '足'},
    {'English': 'stand', 'Kanji': '立'},
    {'English': 'go', 'Kanji': '行'},
    {'English': 'come', 'Kanji': '来'},
    {'English': 'see', 'Kanji': '見'},
    {'English': 'speak', 'Kanji': '話'},
    {'English': 'listen', 'Kanji': '聞'},
    {'English': 'eat', 'Kanji': '食'},
    {'English': 'drink', 'Kanji': '飲'},
    {'English': 'write', 'Kanji': '書'},
    {'English': 'read', 'Kanji': '読'},
    {'English': 'big', 'Kanji': '大'},
    {'English': 'small', 'Kanji': '小'},
    {'English': 'middle', 'Kanji': '中'},
    {'English': 'high', 'Kanji': '高'},
    {'English': 'low', 'Kanji': '低'},
    {'English': 'new', 'Kanji': '新'},
    {'English': 'old', 'Kanji': '古'},
    {'English': 'white', 'Kanji': '白'},
    {'English': 'black', 'Kanji': '黒'},
    {'English': 'red', 'Kanji': '赤'},
    {'English': 'blue', 'Kanji': '青'},
    {'English': 'yellow', 'Kanji': '黄'},
    {'English': 'green', 'Kanji': '緑'},
    {'English': 'week', 'Kanji': '週'},
    {'English': 'day', 'Kanji': '日'},
    {'English': 'year', 'Kanji': '年'},
    {'English': 'time', 'Kanji': '時'},
    {'English': 'now', 'Kanji': '今'},
    {'English': 'before', 'Kanji': '前'},
    {'English': 'after', 'Kanji': '後'},
    {'English': 'north', 'Kanji': '北'},
    {'English': 'south', 'Kanji': '南'},
    {'English': 'east', 'Kanji': '東'},
    {'English': 'west', 'Kanji': '西'},
    {'English': 'money', 'Kanji': '金'},
    {'English': 'friend', 'Kanji': '友'},
    {'English': 'teacher', 'Kanji': '先生'},
    {'English': 'student', 'Kanji': '学生'},
    {'English': 'love', 'Kanji': '愛'},
    {'English': 'heart', 'Kanji': '心'},
    {'English': 'road', 'Kanji': '道'},
    {'English': 'house', 'Kanji': '家'},
    {'English': 'town', 'Kanji': '町'},
    {'English': 'country', 'Kanji': '国'},
    {'English': 'world', 'Kanji': '世界'},
    {'English': 'power', 'Kanji': '力'},
    {'English': 'mind', 'Kanji': '意'},
    {'English': 'spirit', 'Kanji': '魂'},
    {'English': 'life', 'Kanji': '生'},
    {'English': 'death', 'Kanji': '死'},
    {'English': 'peace', 'Kanji': '平'},
    {'English': 'war', 'Kanji': '戦'},
    {'English': 'light', 'Kanji': '光'},
    {'English': 'dark', 'Kanji': '暗'},
    {'English': 'sea', 'Kanji': '海'},
    {'English': 'wind', 'Kanji': '風'},
    {'English': 'flower', 'Kanji': '花'},
    {'English': 'forest', 'Kanji': '森'},
    {'English': 'stone', 'Kanji': '石'},
    {'English': 'fish', 'Kanji': '魚'},
    {'English': 'bird', 'Kanji': '鳥'},
    {'English': 'dog', 'Kanji': '犬'},
    {'English': 'cat', 'Kanji': '猫'}
]
    

def spanish(score):
    for word in spanish_words:
        print(f"What is the English translation of {word['Spanish']}?")
        user_answer= input("Your answer: ").strip().lower()  
        correct_answer= word['English'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score +=1
        else:
            print(f"Wrong, idiot! The correct answer is {word['English']}\n")
    
    print(f'Quiz complete! Your score: {score}/{len(spanish_words)}')

def german(score):
    for word in german_words:
        print(f'What is the English translation of {word["German"]}?')
        user_answer= input("Your answer: ").strip().lower()  
        correct_answer= word['English'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score +=1
        else:
            print(f"Wrong, idiot! The correct answer is {word['English']}\n")
    
    print(f'Quiz complete! Your score: {score}/{len(german_words)}')

def french(score):
    for word in french_word:
        print(f'What is the English translation of {word["French"]}?')
        user_answer= input("Your answer: ").strip().lower()  
        correct_answer= word['English'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score +=1
        else:
            print(f"Wrong, idiot! The correct answer is {word['English']}\n")
    
    print(f'Quiz complete! Your score: {score}/{len(french_word)}')

def italian(score):
    for word in italian_words:
        print(f'What is the English translation of {word["Italian"]}?')
        user_answer= input("Your answer: ").strip().lower()  
        correct_answer= word['English'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score +=1
        else:
            print(f"Wrong, idiot! The correct answer is {word['English']}\n")
    
    print(f'Quiz complete! Your score: {score}/{len(italian_words)}')

def kanji(score):
    for word in kanji_words :
        print(f'What is the English translation of {word["Kanji"]}?')
        user_answer= input("Your answer: ").strip().lower()  
        correct_answer= word['English'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score +=1
        else:
            print(f"Wrong, idiot! The correct answer is {word['English']}\n")
    
    print(f'Quiz complete! Your score: {score}/{len(kanji_words)}')




def main():
    print("Welcome to the language learing Flashcards App!")
    input("Press Enter to start this quiz...")
    
    score = 0
    r=1
    
    while r>0:
        r-=1
        print("Which language do you want to review?\n A.Spanish\n B.German\n C.French\n D.Italian\n E.Japenese Kanji\n")
        
        choice= input("Enter your choice: ").upper().strip()
        if choice == "A":
            random.shuffle(spanish_words)
            spanish(score)
        elif choice =="B":
            random.shuffle(german_words)
            german(score)
        elif choice == "C":
            random.shuffle(french_word)
            french(score)
        elif choice == "D":
            random.shuffle(italian_words)
            italian(score)
        elif choice == "E":
            random.shuffle(kanji_words)
            kanji(score)
        else:
            print("Invalid, enter again\n")
            r+=1
 


if __name__ == "__main__":
    main()