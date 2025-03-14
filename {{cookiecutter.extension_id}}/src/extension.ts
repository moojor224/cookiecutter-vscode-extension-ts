import * as vscode from "vscode";

export function activate(context: vscode.ExtensionContext) {

    let command = vscode.commands.registerTextEditorCommand("{{cookiecutter.extension_id}}.command", (editor: vscode.TextEditor, edit: vscode.TextEditorEdit) => {
        // do things here
        vscode.window.showInformationMessage("command has been run");
    });

    context.subscriptions.push(command);
}

export function deactivate() { }
