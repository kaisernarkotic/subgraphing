from ogb.graphproppred import DglGraphPropPredDataset, collate_dgl
from torch.utils.data import DataLoader

dataset = DglGraphPropPredDataset(name = "ogbg-molhiv")

split_idx = dataset.get_idx_split()
train_loader = DataLoader(dataset[split_idx["train"]], batch_size=32, shuffle=True, collate_fn=collate_dgl)
valid_loader = DataLoader(dataset[split_idx["valid"]], batch_size=32, shuffle=False, collate_fn=collate_dgl)
test_loader = DataLoader(dataset[split_idx["test"]], batch_size=32, shuffle=False, collate_fn=collate_dgl)

print(dataset[0])