
module.exports = plugin => {
	plugin.setOptions({ dev: true, alwaysInit: true })
	function setLine() {
		plugin.nvim.setLine("yolo");
	}
	plugin.registerCommand("SetMyLine", [plugin.nvim.buffer, setLine]);
};
