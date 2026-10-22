// Content Design Review: starter plugin (not tested in Figma; check before you rely on it).
// Sends the text of the current selection to the UI, which checks it against the published rules.

figma.showUI(__html__, { width: 420, height: 560 });

function collectText(nodes) {
  const out = [];
  function walk(node) {
    if (node.type === "TEXT") {
      out.push({ id: node.id, name: node.name, text: node.characters });
    }
    if ("children" in node) node.children.forEach(walk);
  }
  nodes.forEach(walk);
  return out;
}

function sendSelection() {
  figma.ui.postMessage({ type: "selection", items: collectText(figma.currentPage.selection) });
}

figma.on("selectionchange", sendSelection);

figma.ui.onmessage = async (msg) => {
  if (msg.type === "ready") {
    sendSelection();
  } else if (msg.type === "select") {
    const node = await figma.getNodeByIdAsync(msg.id);
    if (node && node.type !== "DOCUMENT" && node.type !== "PAGE") {
      figma.currentPage.selection = [node];
      figma.viewport.scrollAndZoomIntoView([node]);
    }
  } else if (msg.type === "close") {
    figma.closePlugin();
  }
};
