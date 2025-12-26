import { app } from "../../scripts/app.js";

app.registerExtension({
    name: "GoogleAI.HideApiKey",
    
    nodeCreated(node) {
        if (node.comfyClass === "GoogleAIGenerateImage") {
            const originalConfigure = node.configure;
            
            node.configure = function(data) {
                originalConfigure.apply(this, arguments);
                
                setTimeout(() => {
                    const widgets = this.widgets || [];
                    for (const widget of widgets) {
                        if (widget.name === "api_key") {
                            widget.inputEl.type = "password";
                            widget.inputEl.style.fontFamily = "monospace";
                        }
                    }
                }, 100);
            };
        }
    }
});
