import "token-free";
import { Token } from "@phosphor/coreutils";
/**
 * A class which provides a unified way of accessing the different types of tokens.
 */
export declare class TokenSet<T> extends Map<Token<any>, T[]> implements Iterable<[Token<any>, T]> {
    /**
     * Add a value to the set of tokens for a particular token type. If the token
     * does not exist in the map, it is created with an empty array. The `value` is added to that array.
     * @param token - The specific token type to add the `value` to.
     * @param value - The value to be added to the set of values associated with `token`.
     * @return
    
    *   Returns the new list of values associated with the given `token`, including `value`.
    */
    add(token: Token<T>, value: T): T[];
    /**
     * Test whether the set contains a value for a particular token type.
     * @param token - The token of interest.
     * @returns True if the set has a mapping for `token`, false otherwise.
    
    */
    has(token: Token<any>): boolean;
    /**
     * Get the first value associated with a token. This function returns the first value
     * in the list of values associated with a token. If there are no values associated
     * with the token, this method returns `undefined`.
     * @param token - The token of interest.
     * @returns The value associated with the token or `undefined` if none exists.
     */
    get(token: Token<T>): T | undefined;
}
