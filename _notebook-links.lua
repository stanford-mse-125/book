function Pandoc(doc)
  local input = quarto.doc.input_file
  if not input then return doc end
  local base = input:match("([^/]+)%.qmd$")
  if not base or not base:match("^lec%d") then return doc end
  
  local colab_url = "https://colab.research.google.com/github/stanford-mse-125/book/blob/notebooks/" .. base .. ".ipynb"
  local download_url = "notebooks/" .. base .. ".ipynb"
  
  local link_html = '<div class="notebook-links" style="margin-bottom: 1em; padding: 0.5em 1em; background: #f8f9fa; border-radius: 6px; font-size: 0.9em;">'
    .. '<a href="' .. colab_url .. '" target="_blank">'
    .. '<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab" style="vertical-align: middle;"></a>'
    .. '&nbsp;&nbsp;'
    .. '<a href="' .. download_url .. '" download style="vertical-align: middle;">Download notebook (.ipynb)</a>'
    .. '</div>'
  
  local block = pandoc.RawBlock("html", link_html)
  table.insert(doc.blocks, 1, block)
  return doc
end
