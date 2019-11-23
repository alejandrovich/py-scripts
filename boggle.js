/*
    A boggle board consists of 4 rows of 4 letters.
*/

// The board is indexed like a cartesian grid, with (x, y) coordinates as strings.
/*
    O W A G
    L T B P
    S L B E
    D N E T

    words in there: NET, LET, WAG, STAG, PET
*/

// a node for a trie
const Node = (letter, isWord) => {
    const node = {
        letter: letter,
        isWord: isWord,
        pointers: [],
    };
    node.get = letter => {
        let newNode;
        // console.log('searching for ' + letter + ' in ' + node.letter);
        node.pointers.forEach(n => {
            if(n.letter === letter) {
                // console.log('found ' + letter + ' in ' + node.letter);
                newNode = n;
            }
        });
        if( newNode === undefined) {
            newNode = Node(letter, false);
            // console.log('appending ' + letter + ' to ' + node.letter)
            node.pointers.push(newNode);
        }
        return newNode;
    };
    return node;
};


const printTrie = trie => {
    console.log('root');
    trie.root.pointers.forEach(n => {
        console.log(n.letter)
    })
};

const Trie = () => {
    const trie = {
        root: Node('', false),
    };

    trie.addWord = word => {
        /*
            For each letter, find the path for it if it exists
        */
        start = trie.root;
        [...word].forEach((char, index, array) => {
            start = start.get(char);
            if(index === array.length - 1)
                start.isWord = true;
        })
    };
    return trie;
};

mockWordList = ['NET', 'LET', 'WAG', 'STAG', 'PET', 'NEAT', ];
board = {
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

for(let y = 3; y >= 0; y-- ) {
    let row = '';
    for(let x = 0; x < 4; x++ ) {
        row += Node(board[x.toString() + y.toString()], false).letter
    }
    console.log(row);
}

t = Trie()
// word = 'foo';
// [...word].forEach(c => console.log(c));
mockWordList.map(word => t.addWord(word));
console.log(t)
printTrie(t)
