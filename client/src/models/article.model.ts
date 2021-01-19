import TagModel from "./tag.model";

export default interface ArticleModel {
    id: number,
    title: string,
    content: string,
    image: string,
    author: string,
    visible: boolean,

    tags: TagModel[]
}