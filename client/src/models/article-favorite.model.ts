import ArticleModel from "./article.model";

import UserModel from "@/models/article-favorite.model";

export default interface ArticleFavoriteModel extends ArticleModel {
    favorite: boolean
}