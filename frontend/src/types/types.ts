export interface Deck {
    id: number;
    category: number;
    owner: string;
    name: string;
    description: string;
}
export interface DeckListResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: Deck[];
}