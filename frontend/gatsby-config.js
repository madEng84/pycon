module.exports = {
    plugins: [
        {
            resolve: `gatsby-source-filesystem`,
            options: {
                path: `${__dirname}/content/assets`,
                name: `assets`,
            },
        },
        {
            resolve: `gatsby-transformer-remark`,
            options: {
                plugins: [
                    {
                        resolve: `gatsby-remark-images`,
                        options: {
                            maxWidth: 500,
                        },
                    },
                    {
                        resolve: `gatsby-remark-external-links`,
                        options: {
                            target: `_blank`,
                            rel: `nofollow noopener noreferrer`,
                        },
                    },
                    `gatsby-remark-responsive-iframe`,
                ],
            },
        },
        `gatsby-plugin-typescript`,
        `gatsby-plugin-react-helmet`,
        `gatsby-plugin-styled-components`,
        `gatsby-transformer-sharp`,
        `gatsby-plugin-sharp`,
        {
            resolve: `gatsby-plugin-favicon`,
            options: {
                logo: "./static/logo.png",
                appName: "PyCon Italia",
                developerName: null,
                developerURL: null,
                dir: "auto",
                lang: "en-GB",
                background: "#fff",
                theme_color: "#fff",
                display: "standalone",
                orientation: "any",
                start_url: "/?homescreen=1",
                version: "1.0",

                icons: {
                    android: true,
                    appleIcon: true,
                    appleStartup: true,
                    coast: false,
                    favicons: true,
                    firefox: true,
                    opengraph: false,
                    twitter: false,
                    yandex: false,
                    windows: false,
                },
            },
        },
    ],
};