import axios from 'axios';
import type { DeckListResponse } from "@/types/types";

const base_url = 'http://localhost:8000';

const axiosInstance = axios.create({
    baseURL: base_url,
})


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
