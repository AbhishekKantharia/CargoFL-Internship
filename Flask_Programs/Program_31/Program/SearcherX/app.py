import wikipedia
from flask import Flask, render_template, request

app = Flask(__name__)
app.jinja_env.filters["zip"] = zip
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def finder_x(keyword):
    results = wikipedia.search(keyword,results = 8)
    print(f"Total Results fetched {len(results)}")
    tp = []
    linksforpage = []
    pageinfoforhtml = []
    for x in results:
        try:
            tp.append(x)
            getlink = wikipedia.page(x, auto_suggest=False, redirect=False).url
            linksforpage.append(getlink)
            page_summary = wikipedia.summary(
                x, sentences=1, auto_suggest=False, redirect=False
            )
            pageinfoforhtml.append(page_summary)

        except wikipedia.exceptions.PageError as e:
            print(f"wikipedia.page({x}).url not found.")
        except wikipedia.exceptions.DisambiguationError as e:
            pass
    return tp, linksforpage, pageinfoforhtml


# finder_x("Sikkim")


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method != "POST":
        return render_template("index.html")
    userinput = request.form.get("pswd")
    heading, links, info = finder_x(f"{userinput}")
    userinput = userinput.capitalize()

    return render_template(
        "index.html",
        si=userinput,
        lol=zip(heading, links, info),
        sz=list(zip(heading, links, info)),
    )


# main driver function
if __name__ == "__main__":
    app.run()
