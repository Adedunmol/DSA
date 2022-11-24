
// const depthFirstPrint = (graph, source) => {
//     const stack = [ source ]

//     while (stack) {
//         const current = stack.pop()
//         console.log(current)
//         for (let neighbor of graph[current]) {
//             stack.push(neighbor)
//         }
//     }
// }

// const depthFirstPrint = (graph, source) => {
//     console.log(source)
//     for (let neighbor of graph[source]) {
//         depthFirstPrint(graph, neighbor)
//     }
// }

// const breadthFirstPrint = (graph, source) => {
//     const queue = [ source ]

//     while (queue) {
//         const current = queue.shift()
//         console.log(current)
//         for (let neighbor of graph[current]) {
//             queue.push(neighbor)
//         }
//     }
// }

const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
}

// breadthFirstPrint(graph, 'a')
// depthFirstPrint(graph, 'a')


const hasPath = (graph, src, dst) => {
    if (src === dst ) return true;

    for (let neighbor of graph[src]) {
        hasPath(graph, neighbor, dst)
    }
}