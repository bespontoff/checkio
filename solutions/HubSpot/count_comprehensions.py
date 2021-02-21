#!/home/bespontoff/PycharmProjects/checkio/venv/bin/checkio --domain=py run count-comprehensions

# You have to write a function that receives a Python source code,    counts list/set/dict/generator comprehensions and returns these counts.
# List comprehensions, set comprehensions, dict comprehensions, generator expressions    are respectively represented by "ListComp", "SetComp", "DictComp", "GeneratorExp"    in the result dictionary.
# 
# Input:A string.
# Output:A dict with strings as keys and integers as values.
# 
# 
# Note:Python codes are valid (no syntax error) but do not necessarily    comply to PEP8 rules or any implicit rule you may think of.
# 
# 
# END_DESC

from typing import Dict


def count_comprehensions(source: str) -> Dict[str, int]:
    ...


if __name__ == '__main__':
    from textwrap import dedent

    TESTS = [
        ('[n ** 2 for n in range(5)]', {'ListComp': 1}),
        ('{n ** 2 for n in range(6)}', {'SetComp': 1}),
        ('{n: n ** 2 for n in range(7)}', {'DictComp': 1}),
        ('(n ** 2 for n in range(8))', {'GeneratorExp': 1}),
        ('list(n ** 2 for n in range(5))', {'GeneratorExp': 1}),
        ('set(n ** 2 for n in range(6))', {'GeneratorExp': 1}),
        ('dict((n, n ** 2) for n in range(7))', {'GeneratorExp': 1}),
        ('sum(n ** 2 for n in range(5))', {'GeneratorExp': 1}),
        (
            '[x for x in (n ** 2 for n in range(100)) if x % 8]',
            {'ListComp': 1, 'GeneratorExp': 1}
        ),
        (
            dedent('''\
            limit = 100
            assert all(
                sum(n ** 3 for n in range(N)) == (N * (N - 1) // 2) ** 2
                for N in range(1, limit)
            )
            '''),
            {'GeneratorExp': 2}
        ),
        (
            dedent('''\
            from typing import List

            def f(n: int) -> List[int]:
                return [
                    square
                    for square in (number ** 2 for number in range(n))
                    if square % 8
                ]

            if __name__ == '__main__':
                from pprint import pprint
                pprint({n: len(squares) for squares in map(f, range(1, 100))})
            '''),
            {'ListComp': 1, 'GeneratorExp': 1, 'DictComp': 1}
        ),
        (
            dedent('''\
            from typing import Dict, Iterator, List, Set

            def connected_components(graph: Dict[str, List[str]]) -> Iterator[Set[str]]:
                """
                Generate connected components of an undirected graph
                using adjacency list representation.
                """
                seen = set()
                for start in graph:
                    if start in seen:
                        continue
                    stack, component = [start], set()
                    while stack:
                        node = stack.pop()
                        if node not in component:
                            component.add(node)
                            stack += [
                                neighbor
                                for neighbor in graph[node]
                                if neighbor not in component
                            ]
                    yield component
                    seen |= component

            if __name__ == '__main__':
                vertices = list('ABCDEF')
                edges = ['AC', 'BE', 'ED']
                graph = {vertex: [] for vertex in vertices}
                for A, B in edges:
                    graph[A].append(B)
                    graph[B].append(A)
                assert sorted(map(sorted, connected_components(graph))) == [
                    ['A', 'C'], ['B', 'D', 'E'], ['F']]
            '''),
            {'DictComp': 1, 'ListComp': 1}
        ),
    ]
    for n, (source, answer) in enumerate(TESTS):
        counts = count_comprehensions(source)
        # Check for equality but ignore authorized keys with a count of zero.
        assert isinstance(counts, dict), 'must return a dict'
        assert counts.keys() <= {'ListComp', 'SetComp', 'DictComp',
                                 'GeneratorExp'}, 'Wrong dict key'
        assert {k: v for k, v in counts.items() if v != 0} == answer, n
    print('Well done! Click on "Check" for more tests.')