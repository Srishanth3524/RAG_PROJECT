import reflex as rx

config = rx.Config(
       app_name="RAG_PROJECT",
       api_url="0351582a-27bd-4bd5-ae6f-26954d44a4a6.fly.dev",
       plugins=[
           rx.plugins.SitemapPlugin(),
           rx.plugins.TailwindV4Plugin(),
       ]
)
