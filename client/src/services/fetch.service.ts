import { CONSTS } from "@/models/consts";
import { token } from "@/state";

export async function fetchJsonAuth(path: string, method: "get" | "post" | "delete" = "get") {
    const res = await fetch(`${CONSTS.ENDPOINT}/${path}`, {
        method: method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `JWT ${token?.value}`
        },
    });

    try {
        return await res.json();
    } catch (e) {
        return {};
    }
}

export async function postJson(path: string, body: any) {
    const res = await fetch(`${CONSTS.ENDPOINT}/${path}`, {
        method: "post",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    });

    return await res.json();
}


export async function postJsonAuth(path: string, body: any, method: "post" | "put" = "post") {
    const res = await fetch(`${CONSTS.ENDPOINT}/${path}`, {
        method: method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `JWT ${token.value}`
        },
        body: JSON.stringify(body)
    });

    return await res.json();
}


export async function getJson(path: string) {
    const res = await fetch(`${CONSTS.ENDPOINT}/${path}`, {
        method: "get",
        headers: {
            "Content-Type": "application/json"
        }
    });

    return await res.json();
}

// fetch("http://127.0.0.1:5000/users").then(c => c.json().then(d => console.log(d)))