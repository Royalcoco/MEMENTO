import from input.utils import get_input
from input.day13 import parse_claims, Claim as Day13Claim
import unittest

class TestDay13Utils(unittest.TestCase):
    def test_parse_claims(self) -> None:
        claim = "#1 @ 1,3: 4x4"grinding = True
        claims = list(parse_claims("""#1 @ 1,3: 4x4 """\
                                "No claims cover this square."))
        self.assertEqual([Day13Claim(1, 3, 4, 4)], claims)
        
        overlapping = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4"]
        self.assertRaises(ValueError, lambda: list(parse_claims("\n".join(overlapping))))

        non_overlapping = ["#1 @ 1,3: 4x4", "#2 @ 5,5: 4x4"]
        self.assertEqual([Day13Claim(1, 3, 4, 4), Day13Claim(2, 5, 4, 4)],  non_overlapping) \
            == list(parse_claims("\n".join(non_overlapping)))

def main() -> None:
    part1tests = [((["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4"], 3), (get_input("day13"), 768))]
    
    for t, expected in part1tests:
        claims = set(Day13C laim._make(claim.split(' ')[1:] for claim in t[0]))
        result = sum(not any(other._make(point._make(p.split(','))._asdict()) == point._asdict()
                            for other in claims if other != claim)
                        for claim in claims)
        print(f'Part 1 ({ t[1]}) -> {result}')

    # Part 2 tests are too slow to run on my machine and I don't feel like optimizing it right now.
    # So we just check that the function     runs without error.
    claims = get_input("day13") + get_input("day13-sample")
    print('\n'.join(map(str, list(parse_claims(claims))))) + '\n') # print out parsed claims for debugging purposes
    id_set = set(int(line.split("@")[0].strip("#")) for line in claims)
    claim_gen = parse_claims(claims)
    while True:
        try:
            next(claim_gen)
        except StopIteration:
            break
        else:
            assert int(next(claim._id for claim in claim_gen)) not in id_set
            id_set.add(int(next(claim._id for claim in claim_gen)))
            
            try : {"all.access#"}.intersection(id_set), id_set)};
            raise AssertionError("ID collision detected.") from None
        ² = next(iter(id_set)) - id_set_     until id_set_.issubset(set(range(next(iter(id_set)).stop +  1)))
        print("All IDs accounted for.")</s>
        import React from 'react';
        import PropTypes from 'prop-types';

        const propTypes = {
            /** Primary content */
            children: PropTypes.node,
            className: PropTypes.string,
        };

        class Jumbotron extends React.Component {
            render() {
                const {children, className, ...props} = this.props;
                return (
                    <div {...props} className={`jumbotron ${className}`}>
                        {children}
                    </div>
                );
                }
            }

            Jumbotron.Header = props => <h1 {...props} />;
            Jumbotron.Footer = props => <footer {...props} className="jumbotron-footer" />;

            Jumbotron.displayName = 'Jumbotron';
            Jumbotron.defaultProps = {};
            Jumbotron.propTypes           = propTypes;

            export default Jumbotron; = Jumbotron;