from copy import copy

from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page


class NavModifierPlugin(BasePlugin):
    def on_nav(self, nav, config, files):
        labels_by_path = {}

        def collect(items):
            for entry in items:
                if isinstance(entry, dict):
                    for title, path in entry.items():
                        if isinstance(path, str):
                            labels_by_path.setdefault(path, []).append(title)
                elif isinstance(entry, list):
                    collect(entry)

        collect(config.get("nav", []))

        counters = {}

        def rewrite(items):
            if items is None:
                return None

            result = []
            for item in items:
                if isinstance(item, Page):
                    src = item.file.src_path if item.file else None
                    if src and labels_by_path.get(src):
                        count = counters.get(src, 0)
                        titles = labels_by_path[src]

                        if count == 0:
                            item.file.page = item
                            item.title = titles[0]
                            result.append(item)
                        else:
                            clone = copy(item)
                            clone.file.page = clone
                            clone.title = titles[count]
                            result.append(clone)

                        counters[src] = count + 1
                    else:
                        result.append(item)
                elif hasattr(item, "children"):
                    item.children = rewrite(item.children)
                    result.append(item)
                else:
                    result.append(item)
            return result

        nav.items = rewrite(nav.items)
        return nav