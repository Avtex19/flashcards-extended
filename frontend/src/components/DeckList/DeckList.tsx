import { useEffect, useState } from "react";
import type { Deck } from "@/types/types";
import { getDecks } from "@/api/getDeck";

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import {Avatar} from "@mui/material";
import { deepOrange, green, purple } from '@mui/material/colors';

const DeckList: React.FC = () => {
    const [decks, setDecks] = useState<Deck[]>([]);
    const [offset, setOffset] = useState(0);
    const limit = 6;
    const [totalCount, setTotalCount] = useState(0);

    useEffect(() => {
        (async () => {
            try {
                const data = await getDecks(limit, offset);
                if (data) {
                    setDecks(data.results);
                    setTotalCount(data.count);
                }
            } catch (error) {
                console.error('Failed to fetch decks:', error);
            }
        })();
    }, [offset]);

    const handlePrev = () => {
        setOffset((prev) => Math.max(prev - limit, 0));
    };

    const handleNext = () => {
        if (offset + limit < totalCount) {
            setOffset((prev) => prev + limit);
        }
    };


    return (
        <div>
            <Typography variant="h4" gutterBottom sx={{textAlign: 'center'}}>
                Explore flashcards
            </Typography>


            <div style={{display: 'flex', flexWrap: 'wrap', gap: '16px'}}>
                {decks.map((deck) => {
                    const avatarColors = [green[500], deepOrange[500], purple[500]];
                    const randomColor = avatarColors[Math.floor(Math.random() * avatarColors.length)];

                    return (
                        <Card key={deck.id} sx={{
                            width: 300,
                            flexGrow: 1,
                            display: 'flex',
                            flexDirection: 'column',
                            justifyContent: 'space-between'
                        }}>
                            <CardContent sx={{flexGrow: 1}}>
                                <Typography gutterBottom variant="h5" component="div">
                                    {deck.name}
                                </Typography>

                                <Typography variant="body2" color="text.secondary" sx={{marginBottom: 3}}>
                                    {deck.description}
                                </Typography>
                            </CardContent>

                            <CardActions
                                sx={{
                                    display: 'flex',
                                    justifyContent: 'space-between',
                                    alignItems: 'center',
                                    paddingLeft: 2,
                                    paddingRight: 2,
                                }}
                            >
                                <div style={{display: 'flex', alignItems: 'center', gap: 10}}>
                                    <Typography variant="body2" color="text.primary" sx={{marginRight: 0}}>
                                        {deck.owner}
                                    </Typography>
                                    <Avatar sx={{bgcolor: randomColor, width: 24, height: 24, fontSize: 14}}>
                                        {deck.owner ? deck.owner.charAt(0).toUpperCase() : 'U'}
                                    </Avatar>
                                </div>

                                <Button size="small">View</Button>
                            </CardActions>
                        </Card>
                    );
                })}
            </div>


            <div style={{marginTop: 20, display: "flex", justifyContent: "space-between"}}>
                <Button onClick={handlePrev} disabled={offset === 0}>
                    Previous
                </Button>
                <Button onClick={handleNext} disabled={offset + limit >= totalCount}>
                    Next
                </Button>
            </div>
        </div>
    );
};

export default DeckList;
