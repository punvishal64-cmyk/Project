function ResultCard({ result }) {
    if (!result) return null;

    return (
        <div className="bg-white rounded-xl shadow-md p-6 mt-8">

            <h2 className="text-xl font-semibold mb-2">
                📝 Transcript
            </h2>

            <p className="text-gray-700 mb-6">
                {result.transcript}
            </p>

            <h2 className="text-xl font-semibold mb-2">
                🏷 Category
            </h2>

            <p className="mb-6">
                {result.analysis.category}
            </p>

            <h2 className="text-xl font-semibold mb-2">
                📚 Task
            </h2>

            <p>
                {result.analysis.task}
            </p>

        </div>
    );
}

export default ResultCard;