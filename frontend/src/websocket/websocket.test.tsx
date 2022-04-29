import React from "react";
import { rest } from 'msw';
import { setupServer } from "msw/node";
import { fireEvent, render } from "@testing-library/react";
import { Websocket } from "./websocket";


const server = setupServer(
    rest.get('/something', (req, res, ctx) => {
        return res(ctx.json({something: 'something'}))
    })
);

beforeAll(() => server.listen())
afterEach(() => server.resetHandlers())
afterAll(() => server.close())

test('sample test', () => {
    render(<Websocket />);
    // fireEvent.click(screen.getByText('Send'));
});

