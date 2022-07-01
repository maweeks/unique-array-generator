import scripty

test_cases = [
    {
        'input': [],
        'maxLength': 9,
        'expected':[],
        'description': 'Empty array'
    },
    {
        'input': ['asdf'],
        'maxLength': 9,
        'expected':['asdf'],
        'description': 'One item'
    },
    {
        'input': ['asdf', 'fdsa'],
        'maxLength': 9,
        'expected':['asdf', 'fdsa'],
        'description': 'Multiple items - no conflicts'
    },
    {
        'input': ['asdf', 'fdsa'],
        'maxLength': 3,
        'expected':['asd', 'fds'],
        'description': 'Multiple items - no conflicts - cutting'
    },
    {
        'input': ['asdf', 'asdf', 'fdsa'],
        'maxLength': 9,
        'expected':['asdf0', 'asdf1', 'fdsa'],
        'description': 'Multiple items - conflicts'
    },
    {
        'input': ['asdf', 'asdf', 'fdsa'], 'maxLength': 4, 'expected':['asd0', 'asd1', 'fdsa'],
        'description': 'Multiple items - conflicts - cutting'
    },
    {
        'input': ['asdf', 'asdf', 'asd1'],
        'maxLength': 4,
        'expected':['asd0', 'asd1', 'asd2'],
        'description': 'Multiple items - conflicts - cutting - blocked replacement'
    },
    {
        'input': ['asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd'],
        'maxLength': 3,
        'expected':['a00', 'a01', 'a02', 'a03', 'a04', 'a05', 'a06', 'a07', 'a08', 'a09', 'a10'],
        'description': 'RECURSION BABY!!!'
    },
    {
        'input': [
            'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd', 'asd',
            'asd', 'asx', 'asx', 'asx', 'asx', 'asx', 'asx', 'asx', 'asx', 'asx',
            'asx', 'asx', 'asx', 'abc'
        ],
        'maxLength': 3,
        'expected': [
            'a00', 'a01', 'a02', 'a03', 'a04', 'a05', 'a06', 'a07', 'a08', 'a09',
            'a10', 'a11', 'a12', 'a13', 'a14', 'a15', 'a16', 'a17', 'a18', 'a19',
            'a20', 'a21', 'a22', 'abc'
        ],
        'description': 'Merge in recursion'
    }
]

def run_tests():
    passing = 0
    for test in test_cases:
        print('------------------------------------------------')
        print('Input: ', test['input'])
        actual = sorted(scripty.process(test['input'], test['maxLength']))
        expected = sorted(test['expected'])
        result = expected == actual
        print('Result:', result, '- Description:', test['description'])
        if result:
            passing= passing + 1
        else:
            print('Expected:', expected, 'Actual:', actual)
    print('------------------------------------------------')
    print('Tests passed:', passing, 'out of', len(test_cases))

if __name__ == '__main__':
    run_tests()
