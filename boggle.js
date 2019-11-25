/*
    A boggle board consists of 4 rows of 4 letters.

    The board is indexed like a cartesian grid, with (x, y) coordinates as strings.
    Bottom row starts (0,0) and goes up to (3,0), the next row up has y=1.
        O W A G
        L T B P
        S L B E
        D N E T

    Words in there: NET, LET, WAG, STAG, PET, SLEEP, TAG, GAB
*/

// a node for a trie
const Node = (letter, isWord) => {
    const node = {
        letter: letter,
        isWord: isWord,
        pointers: {},  // hash of letter to Node
    };

    // contains: returns a Node corresponding to the letter sought. If it's not in the
    // node, return undefined
    node.contains = letter => {
        if( node.pointers.hasOwnProperty(letter)) {
            return node.pointers[letter]
        }
    };

    // get: returns the Node corresponding to the letter sought. If it's not currently there,
    //  create a new node and return it.
    node.get = letter => {
        // console.log('searching for ' + letter + ' in ' + node.letter);
        const nextNode = node.contains(letter);

        if( nextNode === undefined) {
            const newNode = Node(letter, false);
            // console.log('appending ' + letter + ' to ' + node.letter)
            node.pointers[letter] = newNode;
            return newNode;
        }
        return nextNode;
    };

    // sortedPointers: returns an array of letters (single character strings) sorted
    // alphabetically.
    node.sortedPointers = () => {
        const keys = [];
        for (var k in node.pointers) {
            if (node.pointers.hasOwnProperty(k)) {
                keys.push(k);
            }
        }
        return keys.sort();
    };

    // Done constructing a Node, return the object
    return node;
};

const printNodeWords = (node, current) => {
    // The root node has an empty string ('') as it's letter.
    if(node.letter === '')
        console.log('\nKnown Words');

    if(node.isWord)
        console.log(current + node.letter)
    else {
        const sortedLetters = node.sortedPointers();
        sortedLetters.forEach(key => printNodeWords(node.pointers[key], current + node.letter))
    }
};

const Trie = () => {
    const trie = {
        root: Node('', false),
    };

    /*
        addWord: For each letter, find the path for it if it exists
    */
    trie.addWord = word => {
        node = trie.root;
        [...word].forEach((char, index, array) => {
            node = node.get(char);
            if(index === array.length - 1)
                node.isWord = true;
        })
    };

    // findWord: Returns true if the word is in the Trie, otherwise
    // returns false.
    trie.findWord = word => {
        node = trie.root;
        for(let i = 0; i < word.length; i++) {
            // console.log('finding ' + word[i] + ' in ' + node.letter);
            node = node.contains(word[i]);
            // console.log('at: ' + node.letter);
            if(node === undefined) {
                return false;
            }
        }
        return node.isWord;
    };
    return trie;
};

mockWordList = ['NET', 'LET', 'WAG', 'STAG', 'PET', 'NEAT', ];
sampleBoard = {
    '00': 'D',
    '10': 'N',
    '20': 'E',
    '30': 'T',

    '01': 'S',
    '11': 'L',
    '21': 'B',
    '31': 'E',

    '02': 'L',
    '12': 'T',
    '22': 'B',
    '32': 'P',

    '03': 'O',
    '13': 'W',
    '23': 'A',
    '33': 'G',
};

const displayBoard = board => {
    for(let y = 3; y >= 0; y-- ) {
        let row = '';
        for(let x = 0; x < 4; x++ ) {
            row += board[x.toString() + y.toString()] + ' '
        }
        console.log(row);
    }
};

displayBoard(sampleBoard);
t = Trie();
mockWordList.map(word => t.addWord(word));
printNodeWords(t.root, '');
console.log(t.findWord('NET'));
