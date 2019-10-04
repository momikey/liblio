import { formatDistanceToNow } from "date-fns";

/**
 * Pretty print a date relative to now.
 *
 * @export
 * @param date The date
 * @returns A formatted string, e.g., "5 minutes ago"
 */
export function dateToNow(date) {
    const d = (date instanceof Date) ? date : new Date(date);
    return formatDistanceToNow(d, {
        includeSeconds: true,
        addSuffix: true
    })
}