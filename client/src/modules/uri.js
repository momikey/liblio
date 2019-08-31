/**
 * Create a URI path fragment for a given tag.
 *
 * @export
 * @param key The tag's name (more specifically, a "slug")
 * @returns The URI path fragment for that tag
 */
export function uriForTag (key) {
    return `tag/${key}`;
}

/**
 * Create a Webfinger-style address for a username/server pair.
 *
 * @export
 * @param username The username
 * @param origin The server address
 * @returns An address in the form "@username@origin"
 */
export function actorAddress (username, origin) {
    return `@${username}@${origin}`;
}