import axios from 'axios';

const base_url = 'http://localhost:8000';

const axiosInstance = axios.create({
    baseURL: base_url,
})

interface Deck {
    id: number;
    category: number;
    owner: string;
    name: string;
    description: string;
}
interface DeckListResponse {
    count: number;
    next: string | null;
    previous: string | null;
    results: Deck[];
}
export const getDecks = async (limit = 6, offset = 0): Promise<DeckListResponse | null> => {
    try {
        const response = await axiosInstance.get<DeckListResponse>('/api/decks/', {
            params: { limit, offset },
        });
        console.log('Fetched decks:', response.data);

        return response.data;
    } catch (error) {
        console.error('Failed to fetch deck list:', error);
        return null;
    }
};
