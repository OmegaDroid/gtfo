from gtfo.render import render_response


def handle_it(request, host, path=None):
    return render_response(host, path or "")