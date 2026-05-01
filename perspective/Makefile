SPHINXOPTS  ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR   = .
BUILDDIR    = _build

.PHONY: help html epub latexpdf serve play-html clean

help:
	@$(SPHINXBUILD) -M help $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)

html:
	@$(SPHINXBUILD) -M html $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)
	@echo "Build finished: $(BUILDDIR)/html/index.html"

epub:
	@$(SPHINXBUILD) -M epub $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)
	@echo "Build finished: $(BUILDDIR)/epub/"

latexpdf:
	@$(SPHINXBUILD) -M latexpdf $(SOURCEDIR) $(BUILDDIR) $(SPHINXOPTS)
	@echo "Build finished: $(BUILDDIR)/latex/"

# Serve the HTML build locally at http://localhost:8000
serve: html
	@echo "Serving at http://localhost:8000 — Ctrl+C to stop"
	@cd $(BUILDDIR)/html && python -m http.server 8000

# Build the play/ pool as a standalone mini-site (no toctree checks)
play-html:
	@$(SPHINXBUILD) -M html $(SOURCEDIR) $(BUILDDIR)/play-site \
		-D exclude_patterns="" \
		-D master_doc=play/README \
		$(SPHINXOPTS)
	@echo "Play build finished: $(BUILDDIR)/play-site/html/"

clean:
	@rm -rf $(BUILDDIR)
	@echo "Build directory cleaned."
